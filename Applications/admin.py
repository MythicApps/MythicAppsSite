from django.contrib import admin
from Applications.models import Applicant

# Register your models here.

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['school', 'year']

admin.site.register(Applicant, ApplicantAdmin)