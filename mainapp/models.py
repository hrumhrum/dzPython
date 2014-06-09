from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    addres = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    description = models.CharField(max_length=256)

class News(models.Model):
    organization_id = models.ForeignKey(Organization)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.CharField(max_length=256)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    organization_id = models.ForeignKey(Organization)
    privilegies = models.CharField(max_length=200)


    