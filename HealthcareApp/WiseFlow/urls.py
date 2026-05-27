from django.urls import path
from WiseFlow.views.doctor import DoctorView
from WiseFlow.views.patient import PatientView
from WiseFlow.views.appointment import AppointmentView
from WiseFlow.views.specialization import SpecializationView


urlpatterns = [
    path('doctors/', DoctorView.as_view(), name='doctor-list-create'),
    path('patients/', PatientView.as_view(), name='patient-list-create'),
    path('appointments/', AppointmentView.as_view(), name='appointment-list-create'),
    path('specializations/', SpecializationView.as_view(), name='specialization-list-create')
]