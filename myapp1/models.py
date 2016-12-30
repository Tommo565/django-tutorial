from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50)      # Basic character field
    year_formed = models.PositiveIntegerField() # Basic integer field
   
class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist)                   # Setting a relationship taking another class as a parameter
