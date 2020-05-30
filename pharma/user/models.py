from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class patientsPersonalDetail(models.Model):
    """Personal Details of Users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(default=timezone.now, blank=False)
    address = models.TextField(max_length=255)
    mobile = models.CharField(max_length=12)
    
