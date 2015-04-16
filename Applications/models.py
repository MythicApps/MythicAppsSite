from django.db import models
from django.conf import settings
from General.models import Sponsor
from django.core.validators import RegexValidator

# Create your models here.


class UserType(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    userAffiliation = models.ForeignKey(Sponsor, null=True, blank=True)
    wantsToMentor = models.BooleanField(default=False)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phoneRegex], unique=True, max_length=10, blank=True, null=True)

class School(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class SchoolAbbreviations(models.Model):
    abbr = models.CharField(max_length=50)
    school = models.ForeignKey(School)

class Tech(models.Model):
    name = models.CharField(max_length=100)

class TechToMentor(models.Model):
    tech = models.ForeignKey(Tech)
    mentor = models.ForeignKey(UserType)
    position = models.IntegerField(default=0)

class Hackathon(models.Model):
    name = models.CharField(max_length=100)

class HackathonToApplicant(models.Model):
    hackathon = models.ForeignKey(Hackathon)
    applicant = models.ForeignKey("Applicant")

class Applicant(models.Model):
    user = models.OneToOneField(UserType)
    DoB = models.DateField()
    school = models.ForeignKey(School)
    year_choices = (("FR","Freshman"),
                    ("SP","Sophomore"),
                    ("JR","Junior"),
                    ("SN","Senior"),
                    ("HS","High School"),
                    ("GD","Graduate"),
                    ("OT","Other")
    )
    year = models.CharField(max_length=2,choices=year_choices)
    major = models.CharField(max_length=100)
    github = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    resume = models.FileField(blank=True,null=True)
    otherHackathons = models.BooleanField(default=False)


