from django.shortcuts import render
from django.http import JsonResponse
from General.models import Sponsor, Faq
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