from django.db.models.base import ModelState
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from subscription.models import Person
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['pass']
        user=auth.authenticate(username=user,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect("/authentication/login/")
        
    else:
        return render(request,'login.html')
    
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first name']
        last_name = request.POST['last name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if username=="" or first_name=="" or last_name=="" or email=="" or password1=="" or password2=="":
            messages.info(request,'Please enter all the required fields!!')
            return redirect('/authentication/register/')
        if User.objects.filter(username = username).first():
            messages.info(request,'username is already taken!')
            return redirect('/authentication/register/')
        if User.objects.filter(email = email).first():
            messages.info(request,'Email is already taken!')
            return redirect('/authentication/register/')
        if password1!= password2:
            messages.info(request,'password is not matching with the confirm password')
            return redirect('/authentication/register/')
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        person = Person.objects.create(username=user,subscription_status="NO")
        person.save()
        user.save()
        return redirect('/authentication/login/')
    else:
        return render(request,'register.html')