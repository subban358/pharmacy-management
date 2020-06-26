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
    """All details about the medicines"""
    med_name = models.CharField(max_length=50)
    med_brand = models.CharField(max_length=100)
    med_stock = models.IntegerField(default=0) 
    med_price = models.IntegerField(default=0) 
    med_type = models.CharField(max_length=50)  
    def __str__(self):
        return self.med_name

class Order(models.Model):
    """Keeping Records of the orders"""
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_of_order = models.DateField(default=timezone.now, blank=False)
    cost = models.IntegerField(default=0)
    def __str__(self):
        return self.patient.username+"'s order"

class DoctorDetail(models.Model):
    """All the details of the Doctors"""
    DoctorName = models.CharField(max_length=100)
    DoctorEmail = models.EmailField(max_length=100)
    DoctorPassword = models.CharField(max_length=20)
    Specialization = models.CharField(max_length=50)
    def __str__(self):
        return "Dr. "+self.DoctorName
        
class Rating(models.Model):
    """All The ratings given to the doctor by the user """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0, validators=[MaxValueValidator(5), MinValueValidator(1)])

class Appointment(models.Model):
    """Details About the patients appointments"""
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

