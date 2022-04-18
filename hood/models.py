from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True)
    occupants = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', null=True)
    