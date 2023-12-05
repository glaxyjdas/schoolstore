from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,"invalid username")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        conformpassword=request.POST['password1']
        if password==conformpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
            print("user created")
        else:
            messages.info(request, "password not matched")
            return  redirect('register')
        return redirect('/')
    return render(request,'register.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('/')

def new(request):
    return render(request,'newpage.html')

