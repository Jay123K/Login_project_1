from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .validate import validate_password
from django.contrib.auth.decorators import login_required
# Create your views here.

def Sign_up(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        user= User.objects.filter(username=email)
        if user.exists():
            messages.info(request,"Email alreay exists")
            return redirect('signUp')

        user=User.objects.create(
            first_name=first_name,
            username=email,
        )
        if password1 == password2 and len(password1)==7 and validate_password:
            user.set_password(password1)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"Both password should be same and password should be 7 character.")
            return redirect('signUp')

    return render(request,'app1/templates/sign_up.html')


def Logout_page(request):
    logout(request)
    return redirect(request,'login')


def Login_page(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        if not User.objects.filter(email=email).exists:
            messages.info(request,"Already  Exits")
            return redirect('login')
    
        user=authenticate(username=email,password=password)
        if user is None:
            return redirect('login')
        else:
            login(request,user)
            return redirect ('/')

    return render (request,'app1/templates/login_page.html')


@login_required(login_url='login')
def Home(request):
    return render(request,'app1/templates/home.html')


