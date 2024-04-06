from django.shortcuts import render, redirect   
from apps.users.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


def index(request):
    return render(request, 'index.html', locals())

def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'profile.html', locals())

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password and username and password and email and phone:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.phone = phone
            user.save() 


            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile', user.id)  

    return render(request, 'register.html', locals())


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Пользователь с таким именем не существует.')
            return redirect('login')
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'Неправильный пароль')
            return redirect('login')
    return render(request, 'login.html', locals())