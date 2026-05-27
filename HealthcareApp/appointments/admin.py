from django.contrib import admin
from .models import Specialization, Doctor, Patient, Appointment
# Register your models here.
admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
