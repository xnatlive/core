from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout ,login, authenticate
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is  None:
            # Return an 'invalid login' error message.
            messages.error(request,'خطا در ورود: نام کاربری یا گذرواژه غلط است')
            return render (request,'login.html',{})

        login(request,user)
        return redirect('dashboard')
    else:
        return render (request,'login.html',{})
    
    
# Create your views here.
@login_required
def home(request):
    return render(request,'index.html',{'user':request.user})
