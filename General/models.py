from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField()
    link = models.CharField(max_length=100)
    level_choice = (('b','Bronze'),('s','Silver'),('g','Gold'), ('p','Platnuim'))
    type_choice = (('s','Startup'),('c','Corporate'))
    level = models.CharField(max_length=2, choices=level_choice, default="b")
    type  = models.CharField(max_length=2, choices=type_choice, default="s")

class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
