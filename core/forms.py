from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'Username',
        
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'password',
        'required': 'required',
        
    }))
class SingupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'Username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'password',
        'name': 'display_name',
        'required': 'required',
        'tabindex': '3',
        'data-error': 'password is required',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'conform password*',
        'name': 'display_name',
        'required': 'required',
        'tabindex': '3',
        'data-error': 'password is required',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    
