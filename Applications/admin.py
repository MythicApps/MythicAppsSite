from django.contrib import admin
from Applications.models import Applicant

# Register your models here.
# I recommend that you add the models to this field when you want to check it.
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['school', 'year']

admin.site.register(Applicant, ApplicantAdmin)