import time
from django.shortcuts import render,redirect
from users.models import User
from admins.models import Admins,Employee
from smartbins.models import Smartbin
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from urllib import parse
def user_or_admin(request):
    return render(request,'admin_or_user.html')

# def login_view(request):
#     if request.method=='GET':
#         return render(request,'login_and_signup.html')
#     elif request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if Admins.objects.filter(username=username).exists():                        
#             user = Admins.objects.get(username=username)
#             if user.password==password :
#                 request.session['login_status'] = 'in'
#                 request.session['username'] = user.username
#                 request.session['user_type'] = 'admin'
#                 return redirect('/admin_home_page/')
#                 # return render(request,'admins/admin_index.html')
#             else :
#                 return HttpResponse("Wrong Id or Password")
#         elif Employee.objects.filter(username=username).exists():
#             user = Employee.objects.get(username=username)
#             if user.password==password :
#                 request.session['login_status'] = 'in'
#                 request.session['username'] = user.username
#                 request.session['user_type'] = 'employee'
#                 return render(request,'employee_index.html')
#             else :
#                 return HttpResponse("Wrong Id or Password")
#         elif User.objects.filter(username=username).exists():
#             user = User.objects.get(username=username)
#             if user.password==password :
#                 request.session['login_status'] = 'in'
#                 request.session['username'] = user.username
#                 request.session['user_type'] = 'user'
#                 return render(request,'user_index.html')
#             else :
#                 return HttpResponse("Wrong Id or Password")

#         else:
#             return HttpResponse("This account doesnt exist")

def logout_view(request):
    return render()


def admin_home_page(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
        my_bins = Smartbin.objects.all()
        context = {
            "my_bins":my_bins,
        }
        return render(request,'admins/admin_index.html',context=context)
    else:
        return render(request,'admins/login_and_signup.html')
    
def adminEmployee_view(request):
    None

def map_location(request,id):
    if request.session['login_status'] == 'in' and (request.session['user_type'] == 'admin' or request.session['user_type'] == 'employee' or request.session['user_type'] == 'user' ):
        sbin = Smartbin.objects.get(id=id)
        context = {
            'map_coordinates':sbin.map_location
        }
        return render(request,'map_location.html',context=context)
    else:
        return render(request,'users/login_and_signup.html')
    


def smart_bin_ajax(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
        print("ajax")
        my_bins = Smartbin.objects.all()
        data = serializers.serialize('json', my_bins)
        return HttpResponse(data, content_type="application/json")
        
    else:
        return render(request,'admins/login_and_signup.html')
    
def user_smart_bin_ajax(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'user':
        print("ajax")
        my_bins = Smartbin.objects.all()
        data = serializers.serialize('json', my_bins)
        return HttpResponse(data, content_type="application/json")
        
    else:
        return render(request,'users/login_and_signup.html')
    
def employee_smart_bin_ajax(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'employee':
        print("ajax")
        my_bins = Smartbin.objects.all()
        data = serializers.serialize('json', my_bins)
        return HttpResponse(data, content_type="application/json")
        
    else:
        return render(request,'admins/login_and_signup.html')
    


   


