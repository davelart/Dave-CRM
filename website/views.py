from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

## Authentication

# Registeration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username, email=email).exists():
                messages.info(request, 'User already registered')
                return redirect('register')
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')
    else:    
        return render(request, 'register.html')

# Login Authentication
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Logout Authentication
def logout(request):
    auth.logout(request)
    return redirect('home')
