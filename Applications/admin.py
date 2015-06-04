from django.contrib import admin
from Applications.models import Applicant, School

# Register your models here.
# I recommend that you add the models to this field when you want to check it.
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'year']

admin.site.register(Applicant, ApplicantAdmin)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

admin.site.register(School, SchoolAdmin)