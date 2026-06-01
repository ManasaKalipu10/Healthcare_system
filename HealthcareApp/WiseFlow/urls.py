from django.urls import path

from WiseFlow.views.doctor import DoctorViewSet
from WiseFlow.views.patient import PatientViewSet

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
        DoctorViewSet.as_view({'get': 'get_doctor_details'}),
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
        PatientViewSet.as_view({'get': 'get_patient_details'}),
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
        PatientViewSet.as_view({'post': 'create_appointment'}),
        name='create-appointment'
    ),  

    path(
        'get-all-appointments',
        PatientViewSet.as_view({'get': 'get_all_appointments'}),
        name='get-appointments'
    ),

    path(
        'get-appointment-details',
        PatientViewSet.as_view({'get': 'get_appointment_details'}),
        name='get-appointment-details'
    ),

    path(
        'update-appointment',
        PatientViewSet.as_view({'put': 'update_appointment'}),
        name='update-appointment'
    ),

    path(
        'cancel-appointment',
        PatientViewSet.as_view({'delete': 'cancel_appointment'}),
        name='cancel-appointment'
    ),

    path(
        'check-doctor-slot',
        PatientViewSet.as_view({'get': 'check_doctor_slot'}),
        name='check-doctor-slot'
    ),

    path(
        'get-all-specializations',
        PatientViewSet.as_view({'get': 'get_all_specializations'}),
        name='get-all-specializations'
    ),

    path(
        'create-specialization',
        PatientViewSet.as_view({'post': 'create_specialization'}),
        name='create-specialization'
    ),

    path(
        'get-specialization-details',
        PatientViewSet.as_view({'get': 'get_specialization_details'}),
        name='get-specialization-details'
    ),

    path(
        'update-specialization',
        PatientViewSet.as_view({'put': 'update_specialization_details'}),
        name='update-specialization'
    ),

    path(
        'delete-specialization',
        PatientViewSet.as_view({'delete': 'delete_specialization'}),
        name='delete-specialization'
    )

]