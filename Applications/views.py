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

@csrf_exempt
@api_view(["POST"])
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


def getSchool(schoolName):
    try:
        skool = School.objects.get(name = schoolName)
    except:
        try:
            skool = SchoolAbbreviations.objects.get(abbr = schoolName)
        except:
            skool = School(name = schoolName, type = "college", city = "east lansing", state = "Mi", country = "USA")
    skool.save()
    return skool

#always add the api_view decorator the functions.

@api_view(["POST"])
@login_required
def createApplicant(request):
    from django.contrib.auth.models import User
    if request.method == "POST":
        appForm = ApplicantForm(request.POST)
        if appForm.is_valid():
            #To get the parameter, You need to specify it as an argument to request.POST.get
            # Eg, request.POST.get('user') vs request.POST.get
            # Also this may need to be the model. IDK. I'm not supper familliar with modelForm.
            user = UserType.objects.get(user = request.user)
            newApplication = Applicant(user = user)
            school = getSchool(request.POST.get("schoolName"))
            if(not request.POST.get("notFromSchool")):
                newApplication.travelingFrom = request.POST.get("travelInfo")
            else:
                newApplication.travelingFrom = "{0}, {1} {2}".format(school.city, school.state, school.country)

            newApplication.school = school
            newApplication.otherHackathons = request.POST.get("isFirstHackathon")
            print(request.POST)
            newApplication.resume = request.POST.get("resume")
            newApplication.github = request.POST.get("github")
            newApplication.linkedIn = request.POST.get("linkedIn")
            newApplication.linkedIn = request.POST.get("freeResp")
            newApplication.linkedIn = request.POST.get("dribble")
            newApplication.website = request.POST.get("personalSite")
            newApplication.freeResponce = request.POST.get("freeResponse")
            newApplication.save()
            return JsonResponse({}, status=200)
            pass
        else:
            #Edit for the errors for the Application form
            errors = {"user errors":appForm.errors}
            return JsonResponse(errors,status=406)
    else:
        return JsonResponse({"Error":"Resource not available"},status=501)

@api_view(["GET"])
def getAllSchool(request):
    return School.objects.all()