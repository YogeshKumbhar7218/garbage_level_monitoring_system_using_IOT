from django.shortcuts import render,redirect
from .models import Admins,Employee
from users.models import User,Feedback
from django.http import HttpResponse
from smartbins.models import Smartbin

# Create your views here.
def admin_login_view(request):
    if request.method=='GET':
        return render(request,'admins/login_and_signup.html')
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if Admins.objects.filter(username=username).exists():                        
            user = Admins.objects.get(username=username)
            if user.password==password :
                request.session['login_status'] = 'in'
                request.session['username'] = user.username
                request.session['user_type'] = 'admin'
                return HttpResponse("1")
                # return redirect('/admin_home_page/')
                # return render(request,'admins/admin_index.html')
            else :
                return HttpResponse("Wrong Id or Password")
        elif Employee.objects.filter(username=username).exists():
            user = Employee.objects.get(username=username)
            if user.password==password :
                request.session['login_status'] = 'in'
                request.session['username'] = user.username
                request.session['user_type'] = 'employee'
                return HttpResponse("2")
            else :
                return HttpResponse("Wrong Id or Password")
        else:
            return HttpResponse("This account doesnt exist")

def admin_log_out(request):
    request.session['login_status'] = ''
    request.session['username'] = ''
    request.session['user_type'] = ''
    return redirect("/")


#--------------------- Employee CRUD -------------------------->


def admin_employee(request):#done
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            employees = Employee.objects.all()
            context = {
                "employees":employees,
            }
            return render(request,"admins/admin_employee.html",context=context)
    else:
        return render(request,'admins/login_and_signup.html')

def admin_add_employee(request):#done
    if request.method=='GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            return render(request,"admins/admin_add_employee.html")
        else:
            return render(request,'admins/login_and_signup.html')
    elif request.method=='POST':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
             #Fetch data from the form
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name'] 
            email= request.POST['email']
            contact ="+91"+ request.POST['contact']
            address = request.POST['address']

            #check is username or email already taken
            if (Admins.objects.filter(username=username).exists()) or (Employee.objects.filter(username=username).exists()):
                return HttpResponse('Username has already taken')
            elif (Admins.objects.filter(email=email).exists()) or (Employee.objects.filter(email=email).exists()):
                return HttpResponse('Email has already taken')
            elif (Admins.objects.filter(contact=contact).exists()) or (Employee.objects.filter(contact=contact).exists()):
                return HttpResponse('Phone number has already taken')
            else:
                user = Employee()
                user.username=username
                user.password=password
                user.name=name
                user.email=email
                user.contact=contact
                user.address=address

                user.save()
                return HttpResponse('1')
        else:
            return render(request,'admins/login_and_signup.html')

def adminRemoveEmployee(request, id):#done
    if request.method=='GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            if Employee.objects.filter(id=id).exists():
                employee = Employee.objects.get(id=id)
                employee.delete()
                return HttpResponse('deleted successfully')
            else:
                return HttpResponse('user doesnt exists.')
        else:
            return render(request,'admins/login_and_signup.html')

def admin_edit_employee(request, id):
    if request.method == 'GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
                if Employee.objects.filter(id=id).exists():
                    employee = Employee.objects.get(id=id)
                    employee.contact= employee.contact[3:]
                    context = {
                        "employee":employee,
                    }
                    return render(request,"admins/admin_edit_employee.html",context=context)    
                else:
                    return HttpResponse("Employee does'nt exist")   
        else:
            return render(request,'admins/login_and_signup.html')             
    elif request.method =='POST':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            if Employee.objects.filter(id=id).exists():
                employee = Employee.objects.get(id=id)
            else:
                return HttpResponse("Employee does'nt exist")                     
             #Fetch data from the form
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name'] 
            email= request.POST['email']
            contact ="+91"+ request.POST['contact']
            address = request.POST['address']

            #check is username or email already taken
            if (Admins.objects.filter(username=username).exists())  or ((Employee.objects.filter(username=username).exists()) and (Employee.objects.get(username=username).id != employee.id)):
                return HttpResponse('Username already exists')
            elif (Admins.objects.filter(email=email).exists()) or ((Employee.objects.filter(email=email).exists()) and (Employee.objects.get(email=email).id != employee.id)):
                return HttpResponse('email already exists')
            else:
                employee.username=username
                employee.password=password
                employee.name=name
                employee.email=email
                employee.contact=contact
                employee.address=address
                employee.save()
                return HttpResponse('1')
        else:
            return render(request,'admins/login_and_signup.html')

#--------------------- smartbin CRUD -------------------------->
def admin_smartbin(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            smartbins = Smartbin.objects.all()
            context = {
                "smartbins":smartbins,
            }
            return render(request,"admins/admin_smartbin.html",context=context)
    else:
        return render(request,'admins/login_and_signup.html')

def admin_add_smartbin(request):
    if request.method=='GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            employees = Employee.objects.all()
            context = {
                "employees":employees
            }
            return render(request,"admins/admin_add_smartbin.html",context=context)
        else:
            return render(request,'admins/login_and_signup.html')
    elif request.method=='POST':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
             #Fetch data from the form
            bin_number = request.POST['bin_number']
            location = request.POST['location']
            height = request.POST['height']
            under_employee = request.POST['under_employee']
            map_location = request.POST['map_location']
            if Employee.objects.filter(id=under_employee).exists():
                emp_name = (Employee.objects.get(id=under_employee)).name
                if Smartbin.objects.filter(bin_number=bin_number).exists():
                    return HttpResponse("Please choose another number for smartbin")
                else:
                    smartbin=Smartbin()
                    smartbin.bin_number=bin_number
                    smartbin.location=location
                    smartbin.height=height
                    smartbin.under_employee=under_employee
                    smartbin.map_location=map_location
                    smartbin.name=emp_name
                    smartbin.save()
                    return HttpResponse('1')
            else:
                return HttpResponse("Employee does'nt exists")
        else:
            return render(request,'admins/login_and_signup.html')            

def admin_edit_smartbin(request, id):
    if request.method == 'GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
                employees = Employee.objects.all()
                if Smartbin.objects.filter(id=id).exists():
                    smartbin = Smartbin.objects.get(id=id)
                    context = {
                        "smartbin":smartbin,
                        "employees":employees,
                    }
                    return render(request,"admins/admin_edit_smartbin.html",context=context)    
                else:
                    return HttpResponse("dustbin does'nt exist")
        else:
            return render(request,'admins/login_and_signup.html')          
    elif request.method =='POST':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            if Smartbin.objects.filter(id=id).exists():
                smartbin = Smartbin.objects.get(id=id)
            else:
                return HttpResponse("dustbin does'nt exist")                     
            #Fetch data from the form
            bin_number = request.POST['bin_number']
            location = request.POST['location']
            height = request.POST['height']
            under_employee = request.POST['under_employee']
            map_location = request.POST['map_location']
            if Employee.objects.filter(id=under_employee).exists():
                emp_name = (Employee.objects.get(id=under_employee)).name
                if Smartbin.objects.filter(bin_number=bin_number).exists():
                    if Smartbin.objects.get(bin_number=bin_number).id != id:
                        return HttpResponse("Please choose another number for smartbin")
                    else:
                        # smartbin=Smartbin()
                        smartbin.bin_number=bin_number
                        smartbin.location=location
                        smartbin.height=height
                        smartbin.under_employee=under_employee
                        smartbin.map_location=map_location
                        smartbin.name=emp_name
                        smartbin.save()
                        return HttpResponse('1')
                else:
                        # smartbin=Smartbin()
                        smartbin.bin_number=bin_number
                        smartbin.location=location
                        smartbin.height=height
                        smartbin.under_employee=under_employee
                        smartbin.map_location=map_location
                        smartbin.name=emp_name
                        smartbin.save()
                        return HttpResponse('1')
            else:
                return HttpResponse("Employee does'nt exists")
        else:
            return render(request,'admins/login_and_signup.html')        

def adminRemoveSmartbin(request, id):
    if request.method=='GET':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            if Smartbin.objects.filter(id=id).exists():
                smartbin = Smartbin.objects.get(id=id)
                smartbin.delete()
                return HttpResponse('deleted successfully')
            else:
                return HttpResponse("dustbin does'nt exist")
        else:
            return render(request,'admins/login_and_signup.html')
        



def employee_home_page(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'employee':
        my_bins = Smartbin.objects.all()
        context = {
            "my_bins":my_bins,
        }
        return render(request,'admins/employee_index.html',context=context)
    else:
        return render(request,'admins/login_and_signup.html')


def admin_feedback(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
        feedbacks = Feedback.objects.all().order_by('-time')
        context = {
            "feedbacks":feedbacks,
        }
        return render(request,'admins/admin_feedback.html',context=context)
    else:
        return render(request,'admins/login_and_signup.html')
    
def employee_feedbacks(request):
    if request.session['login_status'] == 'in' and request.session['user_type'] == 'employee':
        feedbacks = Feedback.objects.all().order_by('-time')
        context = {
            "feedbacks":feedbacks,
        }
        return render(request,'admins/employee_feedback.html',context=context)
    else:
        return render(request,'admins/login_and_signup.html')
    
def employee_log_out(request):
    request.session['login_status'] = ''
    request.session['username'] = ''
    request.session['user_type'] = ''
    return redirect("/")

def remove_feedback(request):
    if request.method=='POST':
        if request.session['login_status'] == 'in' and request.session['user_type'] == 'admin':
            id = request.POST['id']
            if Feedback.objects.filter(id=id).exists():
                feedback = Feedback.objects.get(id=id)
                feedback.delete()
                return HttpResponse('deleted successfully')
            else:
                return HttpResponse("feedback does'nt exist")
        else:
            return render(request,'admins/login_and_signup.html')
