from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name= form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            user= authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Invalid Information Entered')
                return redirect('user_login')
    else:
        form= AuthenticationForm(request,request.POST)
        return render(request,'user_login.html',{'form':form})



def user_signup(request):
    if request.method == 'POST':
        signup_form= SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request,'SignUp Successfully')
            return redirect('home')
    else:
        signup_form= SignUpForm(request.POST)
        return render(request,'user_signup.html',{'form':signup_form})