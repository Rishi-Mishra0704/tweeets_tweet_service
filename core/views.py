from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/') 
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/') 
