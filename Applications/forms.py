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

class ApplicantForm(forms.Form):
    freeResponse = forms.Textarea()
    schoolName = forms.CharField()
    isFirstHackathon = forms.BooleanField()
    notFromSchool = forms.BooleanField()
    resume = forms.CharField(required=False)
    travelInfo = forms.Textarea()
    github = forms.CharField(required=False)
    linkedIn = forms.CharField(required=False)
    personalSite = forms.CharField(required=False)

#CAW CAW
    #ROAR
# class ApplicantForm(forms.Form):
#     DoB = forms.DateField()
#     school = School()
    #Name  !*

#Date of Birth !
#Phone number !
#Email !*
#Gender Identity !*
#Where are you traveling from? *

