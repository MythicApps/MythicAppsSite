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

class ApplicantForm(ModelForm):
    freeResponse = forms.Textarea()
    fields = ["DoB", "email", "genderIdentity", "schoolName",
              "year", "major", "github", "website", "linkedIn",
              "resume", "otherHackathons",
              freeResponse,
              "dietaryChoices","dietaryRestrictions",
              "otherDietaryRestrictions","specialAccomodations",
              "travelChoices", "travelMethod","travelingFrom",
              "needReimbursement"]

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

