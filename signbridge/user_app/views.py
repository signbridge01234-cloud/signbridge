from django.shortcuts import render,redirect
from .models import *
from django. contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
import random
import string
from django.core.mail import send_mail
from django.conf import settings
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
            if user.is_active:
                login(request,user)
                messages.success(request,'Login success')
                return redirect('index')
            else:
                messages.error(request,'Account deactivated by admin. contact admin for further details')
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
def org_register(request):
    if request.method == "POST":
        Username= request.POST.get('username')
        org_name= request.POST.get('org_name') 
        org_type= request.POST.get('org_type') 
        Phone_no= request.POST.get('phone_no') 
        Address= request.POST.get('address') 
        Password= request.POST.get('password') 
        Email= request.POST.get('email') 
        Website_link = request.POST.get('Website_link')
        Location= request.POST.get('location') 
        if User.objects.filter(username=Username).exists():
            messages.error(request,'Username already exists')
        if User.objects.filter(email=Email).exists():
            messages.error(request,'email already registered') 
        User.objects.create_user(username=Username,email=Email,org_name=org_name,org_type=org_type,phone_no=Phone_no,address=Address,password=Password,location=Location,website_link=Website_link,usertype="organisation")
        messages.success(request,'Registration successful')
        return redirect('login')
    return render(request,'orgRegister.html')
def deactivate_user(request,id):
    user=User.objects.get(id=id)
    user.is_activate=False
    user.save()
    return redirect('view_students')    
def activate_user(request,id):
    user=User.objects.get(id=id)
    user.is_activate=True
    user.save()
    return redirect('view_students')    
def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})   
def edit_profile(request):
    user=request.user
    if request.method == 'POST':
        username=request.POST.get('username')
        stud_name= request.POST.get('stud_name') 
        Phone_no= request.POST.get('phone_no') 
        Address= request.POST.get('address') 
        Email= request.POST.get('email') 
        Location= request.POST.get('location') 
        Website_link= request.POST.get('website_link') 
        Work_experience= request.POST.get('work_experience')
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            messages.error(request,'Username already exists')
        if User.objects.filter(email=Email).exclude(id=request.user.id).exists():
            messages.error(request,'email already registered') 
        user.email=Email
        user.username=username
        user.stud_name=stud_name
        user.phone_no=Phone_no
        user.address=Address
        user.location=Location
        user.website_link=Website_link
        user.work_experience=Work_experience
        user.save()
        messages.success(request, 'profile updated successfully.')
        return redirect('profile')
    else:
        user=request.user
    return render(request,'edit.html',{'user':user})   

def change_password(request):
    user = request.user
    if request.method == 'POST':
        current.password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        if not user.check_password(current_password):
            messages.error(request, 'current password incorrect')
            return redirect('change_password')
        else:
            user.set_password(new_password)
            user.save()

            update_session_auth_hash(request , user)
            messages.success(request, 'password change success')
            return redirect('profile')

    return render(request , 'change_password.html')

def forgot_password(request):
    if request.method == 'post':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if not user:
            messages.error(request,'No accoutnt found for this email')
            return redirect('forgot_password')

        temp_password = generate_random_password()
        user.set_Password(temp_password)
        user.save()
        Send_mail(Subject = "your one time password",
            message = f'''
                Hello {user.username}
                Your new temporary passwoord is : {temp_password}''',
            from_email = settings.EMAIL_HOST_USER,
            recipeint_list = [email],
            fail_silently  = False,
            )
        messages.success(request, "temporary password send to your email")
        return redirect('login')
    return render(request ,'forgot_password.html')

def generate_random_password(length = 8):
    character = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range (length)) 