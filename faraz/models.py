from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import User
from django.utils import timezone



class Location(models.Model):
    user=models.ForeignKey(User,unique=True)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=30)


