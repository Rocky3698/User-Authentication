from django.shortcuts import render,redirect
from .forms import SignUpForm,ProfileForm,PassForm,PassForm2
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def user_login(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect('user_profile')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signup_form= SignUpForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request,'SignUp Successfully')
                return redirect('user_login')
        else:
            signup_form= SignUpForm(request.POST)
        return render(request,'user_signup.html',{'form':signup_form})
    else :
        return redirect('user_logout')
@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('user_login')

@login_required
def user_profile(request):
    static_count=0
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance= request.user)
        if profile_form.is_valid():
            # profile_form.cleaned_data['password']
            user_name = request.POST['username']
            user_pass = request.POST['password']
            user= authenticate(username=user_name,password=user_pass)
            if user is not None:
                profile_form.save()
                messages.success(request,'Profile Updated Successfully')
                return redirect('user_profile')
            else:
                messages.warning(request,'Passwor Is Incorrect')
                count+=1
                print(count)
                
    else:
        profile_form = ProfileForm(instance=request.user)
    return render(request,'profile.html',{'form':profile_form})

@login_required
def pass_change(request):
    if request.method=='POST':
        form= PassForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('user_profile')
    else:
        form=PassForm(user=request.user)
    return render(request,'pass_change.html',{'form':form,'txt':'Forget password ?'})

@login_required
def pass_change2(request):
    if request.method=='POST':
        form= PassForm2(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('user_profile')
    else:
        form=PassForm2(user=request.user)
    return render(request,'pass_change.html',{'form':form})