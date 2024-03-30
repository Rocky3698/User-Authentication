from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm,SetPasswordForm


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model=User
        fields= ['first_name','last_name','email','username','password1','password2',]
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'First name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last name'}),
            'email':forms.TextInput(attrs={'placeholder':'Email'}),
            'username':forms.TextInput(attrs={'placeholder':'Username'}),
        }
        labels={
            'first_name':'',
            'last_name':'',
            'email':'',
            'username':'',
        }

        help_texts = {
            'username': None,
        }
        # error_messages ={
        #     'username' : {'required': 'Please enter a Username'},
        #     'password1':{'required':''},
        #     'password2':{'required':''}
        # }

class ProfileForm(UserChangeForm):
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password to save changes'}),label='Password',required=True)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']
        help_texts={
            'username':None
        }

class PassForm(PasswordChangeForm):
    new_password1=forms.CharField(label='New password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        
class PassForm2(SetPasswordForm):
    new_password1=forms.CharField(label='New password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
