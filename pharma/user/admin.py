from django.contrib import admin
from .models import patientsPersonalDetail, Medicine, Order, DoctorDetail, Rating, Appointment
# Register your models here.
admin.site.register(patientsPersonalDetail)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(DoctorDetail)
admin.site.register(Rating)
admin.site.register(Appointment)