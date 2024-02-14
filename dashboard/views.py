from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth



# Create your views here.


def home(request):
    
    if  request.user.is_authenticated:

        return render(request,'index.html')
    else:
        return render (request,'login.html')