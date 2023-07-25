import time
import datetime
from django.utils import timezone
from django.shortcuts import render
from .models import Smartbin
from django.http import HttpResponse
from twilio.rest import Client
from admins.models import Employee
import requests
import json

# Create your views here.


def smartbin_view(request):
    if request.method == "GET":
        return render(request, "smartbin/bin_form.html")
    elif request.method == "POST":
        bin_number = int(request.POST["bin_number"])

        sbin = Smartbin.objects.get(bin_number=bin_number)

        dry_filled = (
            (sbin.height - int(request.POST["dry_filled"])) / sbin.height
        ) * 100
        wet_filled = (
            (sbin.height - int(request.POST["wet_filled"])) / sbin.height
        ) * 100

        sbin.dry_filled = dry_filled
        sbin.wet_filled = wet_filled
        sbin.save()
        emp = sbin.under_employee
        emp = Employee.objects.get(id=emp)
        if dry_filled >= 95 or wet_filled >= 95:
            acccout_sid = "AC0814bbbc832e2205fea9778c9d00bca5"
            auth_token = "470121e636ff87aee0dd839c7c432e6c"

            twilio_number = "+19706363509"
            target_number = emp.contact  #'+919673080466'
            client = Client(acccout_sid, auth_token)
            message = client.messages.create(
                body=f"{emp.name} the Dusbin from {sbin.location} area is full please pick up the waste as early as possible!!",
                from_=twilio_number,
                to=target_number,
            )

            print(message.body)
            return HttpResponse(message.body)
        print(sbin)
        return HttpResponse(dry_filled)


def get_smartbin_data(request):
    if request.method == "GET":
        bin_number = int(request.GET["bin_no"])

        sbin = Smartbin.objects.get(bin_number=bin_number)

        dry_filled = (
            (sbin.height - (float(request.GET["dry_filled"]) - 4)) / sbin.height
        ) * 100
        wet_filled = (
            (sbin.height - (float(request.GET["wet_filled"]) - 4)) / sbin.height
        ) * 100

        if dry_filled > 100:
            dry_filled = 100
        elif dry_filled < 0:
            dry_filled = 0

        if wet_filled > 100:
            wet_filled = 100
        elif wet_filled < 0:
            wet_filled = 0

        sbin.dry_filled = dry_filled
        sbin.wet_filled = wet_filled

        print(dry_filled)
        print(wet_filled)

        # check is any of them have fillde above 90%
        # check in data base if request is already sent or not
        # if yes then msg the respective persone and turn on the timer
        emp = sbin.under_employee
        emp = Employee.objects.get(id=emp)
        if dry_filled >= 50 or wet_filled >= 50:
            if sbin.status == "empty":
                sbin.status = "full"
                sbin.date = datetime.datetime.now(tz=timezone.utc)
                # make status = "full", send sms to muncipal person and set current time

                acccout_sid = "Twillio_sid"
                auth_token = "auth_token"
                twilio_number = "+19706363509"
                target_number = emp.contact  #'+919673080466'
                client = Client(acccout_sid, auth_token)
                message = client.messages.create(
                    body=f"{emp.name} the Dusbin from {sbin.location} area is full please pick up the waste as early as possible!!",
                    from_=twilio_number,
                    to=target_number,
                )
                print(message.body)
                print("message sent to the employee")
            else:
                if datetime.datetime.now(tz=timezone.utc) - sbin.date == 2:
                    if sbin.h_a_m_sent == "sent":
                        print("dont send message")
                        # then dont send message again
                    else:
                        # send sms to higher authority
                        print("send message to higher authority")
                        acccout_sid = "Twillio_sid"
                        auth_token = "auth_token"
                        twilio_number = "+19706363509"
                        target_number = "+917558719147"
                        client = Client(acccout_sid, auth_token)
                        message = client.messages.create(
                            body=f"'higher authority name' the Dusbin from {sbin.location} area is full from last two days!!",
                            from_=twilio_number,
                            to=target_number,
                        )
                        print(message.body)
                        sbin.h_a_m_sent = "sent"

        else:
            if sbin.status == "full":
                # garbage has been collected
                print("garbage has been collected")
                sbin.status = "empty"
                sbin.h_a_m_sent = "not"
                sbin.date = datetime.datetime.now(tz=timezone.utc)

        sbin.save()
        return HttpResponse("done")
