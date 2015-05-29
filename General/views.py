from django.shortcuts import render
from django.http import JsonResponse
from General.models import Sponsor, Faq
from django.http import HttpResponse
from django.template.context_processors import csrf
from MythicApps import settings
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    sponsors = []
    
    for x in Sponsor.objects.all():
        print(x.toDictionary())
        sponsors.append(x.toDictionary())
    faqs = []
    for x in Faq.objects.all():
        sponsors.append(x.toDictionary())
    jsonData = {"sponsors":sponsors, "faq":faqs}
    return JsonResponse(jsonData)

def login(request):
    pass

def fuckingCSRF(request):
    response = HttpResponse("I hate CSRF. Who needs security? ")
    response.set_cookie("csrftoken", csrf(request),domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
    return response