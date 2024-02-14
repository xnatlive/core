from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate

# Create your views here.

def login_user(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            # Redirect to a success page.
            return redirect ('home')
        else:
            # Return an 'invalid login' error message.
            messages.info(request,'خطا در ورود')

            return redirect('login')
    else:
        return render (request,'login.html',{})



def register(request):
    return render (request,'register.html')



def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(request,'home')
        else:
            messages.info(request,'خطا در ورود')
            return render (request,'login.html')

    else:
        return render (request,'login.html')


def logout(request):
    
    auth.logout(request)
    return redirect ('home')