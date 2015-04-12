from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField()
    link = models.CharField(max_length=100)
    level_choice = (('b','Bronze'),('s','Silver'),('g','Gold'), ('p','Platnuim'))
    type_choice = (('s','Startup'),('c','Corporate'))
    level = models.CharField(max_length=2, choices=level_choice, default="b")
    type = models.CharField(max_length=2, choices=type_choice, default="s")

    def __str__(self):
        return self.name

    def toDictionary(self):
        return {"name":self.name,
             "logo":str(self.logo),
             "link":self.link,
             "level":self.get_level_display(),
             "type":self.get_type_display()}

class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def toDictionary(self):
        return {"title":self.title,
             "description":str(self.description),
             "category":self.category,
             }