__author__ = 'Yoseph'
from django.forms import ModelForm
from django import forms
from Applications.models import *

class UserCreationForm(forms.Form):
    userName = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=36)
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100, required=False)

class UserTypeForm(ModelForm):
    class Meta:
        model = UserType
        fields = ["wantsToMentor", "phoneNumber", "genderIdentity"]

#CAW CAW 
# class ApplicantForm(forms.Form):
#     DoB = forms.DateField()
#     school = School()
    #Name  !*

#Date of Birth !
#Phone number !
#Email !*
#Gender Identity !*
#Where are you traveling from? *

