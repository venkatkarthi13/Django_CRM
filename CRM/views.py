from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.timezone import localtime
from  .forms import SignupForm, addRecordForm
from .models import Records


def home(request):
    records=Records.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
         
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in successfully")
            return redirect("home")
        else:
            messages.success(request, "Invalid Credentials, Please Try again...")
            return redirect("home")
    else:
        return render(request, "home.html",{'records':records})
    
def log_out(request):
    logout(request)
    messages.success(request,"You have been successfully loggedout...")
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered Welcome!🤗")
            return redirect("home")
    else:
        form=SignupForm()
        return render(request,"register.html",{'form':form})
    
    return render(request,"register.html",{'form':form})
    

def customer_record(request,pk):
    if request.user.is_authenticated:
            customer_record=Records.objects.get(id=pk)
            created_at_ist = localtime(customer_record.created_at)
            return render(request,"record.html",{"customer_record":customer_record, "created_at_ist": created_at_ist})
    else:
        messages.success(request,"You must be logged in to view that page")
        return redirect("home")
        
        
def delete_record(request,pk):
    if request.user.is_authenticated:
            delete_it=Records.objects.get(id=pk)
            delete_it.delete()
            messages.success(request,"Records deleted successfully..")
            return redirect("home")
    else:
        messages.success(request,"You must be logged in to delete records..")
        return redirect("home")
    
def add_record(request):
    form=addRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Your Records has been saved...")
                return redirect("home")
        return render(request, "add_record.html",{"form":form})
    else:
        messages.success(request,"You must be logged in to add record..")
        return redirect("home")
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Records.objects.get(id=pk)
        form=addRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect("home")
        return render(request, "update_record.html",{"form":form})
    else:
        messages.success(request,"You must be logged in to update record..")
        return redirect("home")