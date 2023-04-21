from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context={
    "variable" : "gagan ice cream"
    }
    return render(request, 'index.html',context)
#   return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been send!')
    
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")
# Create your views here.

def loginUser(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    # A backend authenticated the credentials
        else:
            return render(request, 'login.html')


    # No backend authenticated the credentials

    #checking user is 


    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
