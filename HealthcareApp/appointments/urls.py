from django.urls import path

from appointments.views.doctor import DoctorViewSet
from appointments.views.patient import PatientViewSet
from appointments.views.appointment import AppointmentViewSet
from appointments.views.specialization import SpecializationViewSet

urlpatterns = [

    # Doctor APIs
    path(
        'create-doctor',
        DoctorViewSet.as_view({'post': 'create_doctor'}),
        name='create-doctor'
    ),

    path(
        'get-all-doctors',
        DoctorViewSet.as_view({'get': 'get_all_doctors'}),
        name='get-all-doctors'
    ),

    path(
        'get-doctor-details',
        DoctorViewSet.as_view({'post': 'get_doctor_details'}),
        name='get-doctor-details'
    ),

    path(
        'update-doctor',
        DoctorViewSet.as_view({'put': 'update_doctor'}),
        name='update-doctor'
    ),

    path(
        'delete-doctor',
        DoctorViewSet.as_view({'delete': 'delete_doctor'}),
        name='delete-doctor'
    ),

    # Patient APIs
    path(
        'create-patient',
        PatientViewSet.as_view({'post': 'create_patient'}),
        name='create-patient'
    ),

    path(
        'get-all-patients',
        PatientViewSet.as_view({'get': 'get_all_patients'}),
        name='get-all-patients'
    ),

    path(
        'get-patient-details',
        PatientViewSet.as_view({'post': 'get_patient_details'}),
        name='get-patient-details'
    ),

    path(
        'update-patient',
        PatientViewSet.as_view({'put': 'update_patient'}),
        name='update-patient'
    ),

    path(
        'delete-patient',
        PatientViewSet.as_view({'delete': 'delete_patient'}),
        name='delete-patient'
    ),

    #Appointment APIs
    path(
        'create-appointment',
        AppointmentViewSet.as_view({'post': 'create_appointment'}),
        name='create-appointment'
    ),  

    path(
        'get-all-appointments',
        AppointmentViewSet.as_view({'get': 'get_all_appointments'}),
        name='get-appointments'
    ),

    path(
        'get-appointment-details',
        AppointmentViewSet.as_view({'post': 'get_appointment_details'}),
        name='get-appointment-details'
    ),

    path(
        'update-appointment',
        AppointmentViewSet.as_view({'put': 'update_appointment'}),
        name='update-appointment'
    ),

    path(
        'cancel-appointment',
        AppointmentViewSet.as_view({'post': 'cancel_appointment'}),
        name='cancel-appointment'
    ),

    path(
        'check-doctor-slot',
        AppointmentViewSet.as_view({'post': 'check_doctor_slot'}),
        name='check-doctor-slot'
    ),

    # Specialization APIs
    path(
        'get-all-specializations',
        SpecializationViewSet.as_view({'get': 'get_all_specializations'}),
        name='get-all-specializations'
    ),

    path(
        'create-specialization',
        SpecializationViewSet.as_view({'post': 'create_specialization'}),
        name='create-specialization'
    ),

    path(
        'get-specialization-details',
        SpecializationViewSet.as_view({'post': 'get_specialization_details'}),
        name='get-specialization-details'
    ),

    path(
        'update-specialization',
        SpecializationViewSet.as_view({'put': 'update_specialization'}),
        name='update-specialization'
    ),

    path(
        'delete-specialization',
        SpecializationViewSet.as_view({'delete': 'delete_specialization'}),
        name='delete-specialization'
    )

]