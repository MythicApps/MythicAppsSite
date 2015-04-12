from django.db import models
from django.conf import settings
from General.models import Sponsor
from django.core.validators import RegexValidator

# Create your models here.


class UserType(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    userAffiliation = models.ForeignKey(Sponsor, null=True, blank=True)

class School(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Applicant(models.Model):
    user = models.OneToOneField(UserType)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], unique=True, max_length=10)
    