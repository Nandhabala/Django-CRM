from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.success(request, "There was an error logging in. Please try again.")
            return redirect('home')
    
    return render(request, 'home.html', {})  # Render home.html for non-authenticated users


def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out....")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})
