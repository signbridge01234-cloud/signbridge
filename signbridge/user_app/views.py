from django.shortcuts import render,redirect
from .models import *
from django. contrib import messages 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == "POST":
        Username= request.POST.get('username')
        stud_name= request.POST.get('stud_name') 
        Phone_no= request.POST.get('phone_no') 
        Address= request.POST.get('address') 
        Password= request.POST.get('password') 
        Email= request.POST.get('email') 
        Location= request.POST.get('location') 
        Website_link= request.POST.get('website_link') 
        Work_experience= request.POST.get('work_experience') 
        if User.objects.filter(username=Username).exists():
            messages.error(request,'Username already exists')
        if User.objects.filter(email=Email).exists():
            messages.error(request,'email already registered') 
        User.objects.create_user(username=Username,email=Email,stud_name=stud_name,phone_no=Phone_no,address=Address,password=Password,location=Location,website_link=Website_link,work_experience=Work_experience,usertype="student")
        messages.success(request,'Registration succeful')
        return redirect('login')
    return render(request,'register.html')
def login_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login success')
            return redirect('index')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    messages.success(request,'Logout Success')
    return  redirect('index')
def view_students(request):
    students=User.objects.filter(usertype="student")
    return render(request,'view_students.html', {'students':students})    