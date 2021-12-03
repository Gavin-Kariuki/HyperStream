from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegistrationForm(UserCreationForm):
    barua = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','full name','email','password']