from django.core.files.storage import FileSystemStorage
import os
from adminisrtration.models import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import loginids, contactdb
from django.contrib.auth.models import User

def login(request):
    return render(request, 'frontend/login.html')


def save1(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return redirect(login)
   


def save2(request):
    email = request.POST['email']
    password = request.POST['password']
    User = auth.authenticate(email=email,password=password)
    if User is not None:
        auth.login(request,User)
        return redirect(index)
    else:
        return render(request,'frontend/login.html',{'data':'Invalid Entry'})
    

def index(request):
    z = product.objects.all()

    return render(request, 'frontend/index.html', {'data': z})


def contact(request):
    return render(request, 'frontend/contact.html')


def thanks(request):
    return render(request, 'frontend/thanks.html')


def save3(request):
    name1 = request.POST['name1']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    k = contactdb(name=name1, email=email, subject=subject, message=message)
    k.save()
    return redirect(index)
