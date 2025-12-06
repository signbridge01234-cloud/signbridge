from django.shortcuts import render,redirect
from .models import *
from django. contrib import messages 
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == "POST":
        Username= request.POST.get('username')
        stud_name= request.POST.get('Stud_name') 
        Phone_no= request.POST.get('Phone_no') 
        Address= request.POST.get('Address') 
        Password= request.POST.get('Password') 
        Email= request.POST.get('email') 
        Location= request.POST.get('Location') 
        Website_link= request.POST.get('Website_link') 
        Work_experience= request.POST.get('Work_experience') 
        if User.objects.filter(username=Username).exists():
            messages.error(request,'Username already exists')
        if User.objects.filter(email=Email).exists():
            messages.error(request,'email already registered') 
        User.objects.create(username=Username,email=Email,stud_name=stud_name,phone_no=Phone_no,address=Address,password=Password,location=Location,website_link=Website_link,work_experience=Work_experience,usertype="user")
        messages.success(request,'Registration succeful')
        return redirect('login')
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')