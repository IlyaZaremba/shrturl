from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Login Success')
                return redirect('/')
        messages.error(request, 'Incorrect login or password')
        return render(request, 'login.html', {'username': username})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            auth.login(request, user)
        except:
            messages.error(request, 'user already exists')
            return render(request, 'register.html', {'username': username, 'email': email})
        messages.success(request, 'User created')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
