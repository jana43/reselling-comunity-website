from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from .models import UserProfile , Post , Images , Comment
import random
from django.contrib import messages
from django.conf  import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from PIL import Image
import datetime

def index(request):
    return render(request , 'index.html')


    


def register(request):
    if request.method == "POST":
        username = request.POST.get("user")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        bio = request.POST.get("bio")
        location = request.POST.get("address")
        mail_subject = 'Activate your blog account.'
        print('.............................',password1)
        if username == "":
            messages.info(request,'invalid credential please enter an valid username')
            return redirect('register')
        elif User.objects.filter(username = username).exists():
            messages.info(request,'invalid credential username already taken')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request,'invalid credential email already exist')
            return redirect('register')
        elif password1 != password2:
            messages.info(request,'invalid credential confirm passwords not matching ')
            return redirect('register')
        else:
            user = User.objects.create(username=username , email=email , first_name= first_name , last_name= last_name)
            user.set_password(password1)
            User.save(user)
            userdata = UserProfile.objects.create(username=user, bio=bio , location=location)
            UserProfile.save(userdata)
            messages.info(request,'invalid credential please enter an valid username')
            return render(request , 'login.html')
    else:
        return render(request , 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('user',False)
        password = request.POST.get('password1',False)
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential make sure you have entered correct password or username ')
            return redirect(login)
    else:
        return render(request,'login.html')
    
def logout_user(request):
    auth.logout(request)
    return redirect('/')
    
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        files = request.FILES.getlist('images' , False)
         
        createPost = Post.objects.create(title = title , description = description , price =price)
        Post.save(createPost)
        print('........' ,files)

        for f in files:
            chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            randomstr= ''.join((random.choice(chars)) for x in range(10))
            fileName = str(f).replace(" ",'')
            fileName = fileName+title.replace(" ",'')[:6]+randomstr+'.png'
            img = Image.open(f)
            
            img.save(f'media/postimages/{fileName}','png', optimize = True , quality = 10)
            
            f = f"/postimages/{fileName}"
            
            Images.objects.create(post=createPost,image=f)
            
        return redirect('/')
    else:
        return render(request  , 'create.html')



