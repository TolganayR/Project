from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']

class bookForm(forms.ModelForm):
    class Meta:
      model=Booking
      fields='__all__'

