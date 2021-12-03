from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegistrationForm(UserCreationForm):
    barua = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','first_name','email','password'] #primary att for the user are username,password,email,first_name and last_name

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

        
