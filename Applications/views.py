from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from Applications.models import *
from Applications.forms import UserCreationForm, UserTypeForm
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

def createApplicant(request):

    return JsonResponse()