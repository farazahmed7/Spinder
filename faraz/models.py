from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone



class Location(models.Model):
    name = models.CharField(max_length=30)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=30)


