from django.contrib import admin
from .models import patientsPersonalDetail, Medicine, Order, DoctorDetail
# Register your models here.
admin.site.register(patientsPersonalDetail)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(DoctorDetail)
