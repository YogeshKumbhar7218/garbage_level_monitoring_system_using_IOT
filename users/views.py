from django.shortcuts import render,redirect
from .models import User, Feedback
from admins.models import Admins,Employee
from django.http import HttpResponse
from smartbins.models import Smartbin
import datetime
from .forms import ImageForm



def user_logout_view(request):
    request.session['login_status'] = ''
    request.session['username'] = ''
    request.session['user_type'] = ''
    return HttpResponse("Succesfully Loged Out")

# Create your views here.
def user_login_view(request):
    if request.method=='GET':
        return render(request,'users/login_and_signup.html')
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.password==password :
                request.session['login_status'] = 'in'
                request.session['username'] = user.username
                request.session['user_type'] = 'user'
                # return render(request,'user_index.html')
                return HttpResponse("1")
            else :
                return HttpResponse("Wrong Id or Password")

        else:
            return HttpResponse("This account doesnt exist")
        
def user_home_view(request):
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'user':
            my_bins = Smartbin.objects.all()
            context = {
                "my_bins":my_bins,
            }
            return render(request,'users/user_index.html',context=context)
        else:
            return render(request,'users/login_and_signup.html')
        

def signup_view(request):
    if request.method=='GET':
        return render(request,'users/login_and_signup.html')
    elif request.method=='POST':
        #Fetch data from the form
        username= request.POST['username']
        password= request.POST['password']
        name = request.POST['name'] 
        email= request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']

        #check is username or email already taken
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already taken')
        elif User.objects.filter(email=email).exists() :
            return HttpResponse('email already taken')
        else:
            user = User()
            user.username=username
            user.password=password
            user.name=name
            user.email=email
            user.contact=contact
            user.address=address

            user.save()
            return HttpResponse('1')
        


def user_feedback(request):
        
    if request.method=='GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'user':
            form = ImageForm()
            return render(request,'users/user_feedback_form.html',{'form':form})
    elif request.method=='POST':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'user':
            feedback = request.POST['feedback']
            if feedback=="":
                return HttpResponse('Field is empty!')

            user = User.objects.get(username=request.session['username'])
            
            # fback = Feedback()
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():

                print("got image-----------------------------")
                fback = Feedback(photo=request.FILES['photo'])

                fback.username = user.username
                fback.name = user.name
                fback.feedback = feedback
                fback.time = datetime.datetime.now()
                fback.save()
                # form.save()
                return render(request,'users/feedback_success.html')
                
                
                
            
            # fback.username = user.username
            # fback.name = user.name
            # fback.feedback = feedback
            # fback.time = datetime.datetime.now()
            # fback.save()
            # return HttpResponse('1')
            return HttpResponse('not valide')

        else:
            
            return render(request,'users/login_and_signup.html')
        
def user_log_out(request):
    request.session['login_status'] = ''
    request.session['username'] = ''
    request.session['user_type'] = ''
    return redirect("/")