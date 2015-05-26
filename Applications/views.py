from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from Applications.models import *
from Applications.forms import UserCreationForm, UserTypeForm, ApplicantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["post"])
def create(request):
    from django.contrib.auth.models import User
    if request.method == "POST":
        username = request.POST.get("userName")
        pw = request.POST.get("password")
        userForm = UserCreationForm(request.POST)
        userTypeForm = UserTypeForm(request.POST)
        if userForm.is_valid() and userTypeForm.is_valid():
            newUser = User.objects.create_user(username=request.POST.get("userName"),
                                               email=request.POST.get("email"),
                                               password=request.POST.get("password"),
                                               first_name=request.POST.get("firstName"),
                                               last_name=request.POST.get("lastName"))
            newUser.save()
            newUserType = UserType(user = newUser,
                                   wantsToMentor= request.POST.get("wantsToMentor"),
                                   phoneNumber = request.POST.get("phoneNumber"),
                                   genderIdentity = request.POST.get("genderIdentity"))
            newUserType.save()
            newUser = authenticate(username = username, password = pw)
            login(request, newUser)
            return JsonResponse({},status=200)
        else:
            errors = {"user errors":userForm.errors, "user Type Errors":userTypeForm.errors}
            return JsonResponse(errors,status=406)
    else:
        return JsonResponse({"Error":"Resource not available"},status=501)

@csrf_exempt
@login_required
@permission_required('users.can_add')
def sponsorCreate(request):
    from django.contrib.auth.models import User
    if request.method == "POST":
        username = request.POST.get("userName")
        pw = request.POST.get("password")
        userForm = UserCreationForm(request.POST)
        userTypeForm = UserTypeForm(request.POST)
        if userForm.is_valid() and userTypeForm.is_valid():
            newUser = User.objects.create_user(username=request.POST.get("userName"),
                                               email=request.POST.get("email"),
                                               password=request.POST.get("password"),
                                               first_name=request.POST.get("firstName"),
                                               last_name=request.POST.get("lastName"))
            newUser.save()
            newUserType = UserType(user = newUser,
                                   wantsToMentor= request.POST.get("wantsToMentor"),
                                   phoneNumber = request.POST.get("phoneNumber"),
                                   genderIdentity = request.POST.get("genderIdentity"),
                                   userAffiliation=request.user)
            newUserType.save()
            return JsonResponse({},status=200)
        else:
            errors = {"user errors":userForm.errors, "user Type Errors":userTypeForm.errors}
            return JsonResponse(errors,status=406)
    else:
        return JsonResponse({"Error":"Resource not available"},status=501)

    #Personal Info
#Name  !*
#Date of Birth !
#Phone number !
#Email !*
#Gender Identity !*
#Where are you traveling from? *


#always add the api_view decorator the functions.
@api_view(["post"])
@login_required
def createApplicant(request):
    from django.contrib.auth.models import User
    if request.method == "POST":
        username = request.POST.get("userName")
        pw = request.POST.get("password")
        if username.is_valid() and pw.is_valid():
            AppForm = ApplicantForm(request.POST)
            if AppForm.is_valid():
                #To get the parameter, You need to specify it as an argument to request.POST.get
                # Eg, request.POST.get('user') vs request.POST.get
                # Also this may need to be the model. IDK. I'm not supper familliar with modelForm.
                newApp = ApplicantForm(user = Applicant.user(request.POST.get),
                                       DoB = Applicant.DoB(request.POST.get),
                                       email = UserCreationForm.email(request.POST.get),
                                       genderIdentity = UserTypeForm.Meta.model.genderIdentity(request.POST.get),
                                       schoolName = Applicant.school(request.POST.get),
                                       year = Applicant.year_choices(request.POST.get),
                                       major = Applicant.major(request.POST.get),
                                       github = Applicant.github(request.POST.get),
                                       website = Applicant.website(request.POST.get),
                                       linkedIn = Applicant.linkedIn(request.POST.get),
                                       resume = Applicant.resume(request.POST.get),
                                       otherHackathons = Applicant.otherHackathons(request.POST.get),
                                       freeResponse = ApplicantForm.freeResponse(request.POST.get),
                                       dietaryChoices = Applicant.dietary_choices(request.POST.get),
                                       dietaryRestrictions = Applicant.dietaryRestrictions(request.POST.get),
                                       otherDietaryRestrictions = Applicant.otherDietaryRestrictions(request.POST.get),
                                       specialAccomodations = Applicant.specialAccommodations(request.POST.get),
                                       travelChoices = Applicant.travel_choices(request.POST.get),
                                       travelMethod = Applicant.travelMethod(request.POST.get),
                                       travelingFrom = Applicant.travelingFrom(request.POST.get),
                                       needReimbursement = Applicant.needReimbursement(request.POST.get))
                newApp.save()
            else:
                return JsonResponse({"Error":"Resource not available"},status=501)
        else:
            #Edit for the errors for the Application form
            errors = {"user errors":userForm.errors, "user Type Errors":userTypeForm.errors}
            return JsonResponse(errors,status=406)
