from django.contrib import admin
from General.models import Sponsor

# Register your models here.

class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'type']


admin.site.register(Sponsor, SponsorAdmin)
