from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth


# Create your views here.
def login(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        user=auth.authenticate(username=Username,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"inavalid credentials")
            return redirect('login')
    return render (request,"login.html")
def register(request):
    if request.method=='POST':
        Username=request.POST['Username']
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        CPassword = request.POST['Confirm_password']
        if Password==CPassword:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"User name taken")
                return redirect ('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,password=Password,first_name=First_name,last_name=Last_name,email=Email)
                user.save();
                return redirect ('login')
        else :
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect ('/')