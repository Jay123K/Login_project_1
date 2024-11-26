from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def Sign_up(request):
    if request.method=="POST":
        first_name=request.post.get('first_name')
        email=request.post.get('email')
        password1=request.post.get('password1')
        password2=request.post.get('password2')


        user=User.objects.create(
            first_name=first_name,
            email=email,
        )
        if password1 == password2:
            user.set_password(password1)
            user.save()
            return redirect('login')
        else:
            messages.info("Both password should be same")
            return redirect('siginUp')

    return render(request,'templates/sign_up.html')



def Login_page(request):
    if request.method=="POST":
        email=request.post.get('email')
        password=request.post.get('password')

        if not User.objects.filter(email=email).exists:
            return redirect('login')
    
        user=authenticate(email=email,password=password)
        if user is None:
            return redirect('login')
        else:
            login(request,user)
            return redirect ('home')

    return render (request,'app1/templates/login_page.html')


def Home(request):
    return render(request,'templates/home.html')


