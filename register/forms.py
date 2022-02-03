import email
from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    firstname=forms.CharField(max_length=10)
    secondname=forms.CharField(max_length=10)
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["firstname","secondname","username","email","password1","password2"]
