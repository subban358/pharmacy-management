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

class Medicine(models.Model):
    med_name = models.CharField(max_length=50)
    med_brand = models.CharField(max_length=100)
    med_stock = models.IntegerField(default=0) 
    med_price = models.IntegerField(default=0) 
    med_type = models.CharField(max_length=50)  
    def __str__(self):
        return self.med_name

class Order(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_of_order = models.DateField(default=timezone.now, blank=False)
