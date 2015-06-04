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
    idChoices = (
        ("m", "Male"),
        ("f", "Female"),
        ("na","Prefer Not to Disclose")
    )
    deviceKey = models.TextField(blank=True, null=True) #Not used; for mobile phones
    genderIdentity = models.CharField(max_length=2, choices = idChoices)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SchoolAbbreviations(models.Model):
    abbr = models.CharField(max_length=50)
    school = models.ForeignKey(School)

class Tech(models.Model):
    name = models.CharField(max_length=100)

class TechToMentor(models.Model):
    tech = models.ForeignKey(Tech)
    mentor = models.ForeignKey(UserType)
    position = models.IntegerField(default=0)

class TechToApplicant(models.Model):
    tech = models.ForeignKey(Tech)
    applicant = models.ForeignKey("Applicant")

class Hackathon(models.Model):
    name = models.CharField(max_length=100)

class Hardware(models.Model):
    name = models.CharField(max_length=100)

class HackathonToApplicant(models.Model):
    hackathon = models.ForeignKey(Hackathon)
    applicant = models.ForeignKey("Applicant")

class HardwareToApplicant(models.Model):
    hardware = models.ForeignKey(Hardware)
    applicant = models.ForeignKey("Applicant")


class Applicant(models.Model):
    user = models.OneToOneField(UserType)
    DoB = models.DateField(null=True)
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
    siteRegex = RegexValidator(regex=r'^(http(?:s)?\:\/\/[a-zA-Z0-9]+(?:(?:\.|\-)[a-zA-Z0-9]+)+(?:\:\d+)?(?:\/[\w\-]+)*(?:\/?|\/\w+\.[a-zA-Z]{2,4}(?:\?[\w]+\=[\w\-]+)?)?(?:\&[\w]+\=[\w\-]+)*)$',
                              message="Not a proper website url")
    website = models.CharField(max_length=100, blank=True, null=True, validators=[siteRegex])
    linkedIn = models.CharField(max_length=200, blank=True, null=True, validators=[siteRegex])
    resume = models.CharField(max_length=100,blank=True,null=True)
    otherHackathons = models.BooleanField(default=False)
    dietary_choices = (
        ('n','None'),
        ('v',"Vegetarian"),
        ('g', "Vegan"),
        ("k", "Kosher"),
        ("h", "Halal"),
        ('o', "Other"),
    )
    applicationStatus_choices = (
        ('r','Received'),
        ('v',"Reviewed"),
        ('a', "Accepted"),
        ("w", "Wait list"),
        ("d", "Declined"),
        ("f", "Flagged for Abuse"),
    )
    dietaryRestrictions = models.CharField(max_length=1, choices=dietary_choices)
    otherDietaryRestrictions = models.TextField(blank=True, null=True)
    applicationStatus = models.CharField(max_length=1, choices=applicationStatus_choices)
    specialAccommodations = models.TextField(blank=True, null = True)
    travel_choices = (
        ('p','plane'),
        ('t',"train"),
        ('c', "car"),
    )
    travelMethod = models.CharField(max_length=1, choices=travel_choices)
    travelingFrom = models.TextField()
    needReimbursement = models.BooleanField(default=False)
    freeResponce = models.TextField()
    dribble = models.CharField(max_length=200, blank=True, null=True)
