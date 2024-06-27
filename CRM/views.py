from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import views

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
         
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in successfully")
            return redirect("home")
        else:
            messages.success(request, "There was an error occurred, Please Try again...")
            return redirect("home")
    else:
        return render(request, "home.html",{})
    
def log_out(request):
    logout(request)
    messages.success(request,"You have been successfully loggedout...")
    return redirect("home")

def register_user(request):
    return render(request,"register.html",{})