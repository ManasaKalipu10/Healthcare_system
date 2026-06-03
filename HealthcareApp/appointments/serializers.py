from rest_framework import serializers
from appointments.models import Specialization, Doctor, Patient, Appointment

# Model serializers for Doctor, Patient and Appointment models

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'      

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'

# Specialization API serializers

class CreateSpecializationApiSerializer(
    serializers.Serializer
):

    name = serializers.CharField()


class UpdateSpecializationApiSerializer(
    serializers.Serializer
):

    specialization_id = serializers.IntegerField()

    name = serializers.CharField()


class GetSpecializationDetailsApiSerializer(
    serializers.Serializer
):

    specialization_id = serializers.IntegerField()

class DeleteSpecializationApiSerializer(
    serializers.Serializer
):
    specialization_id = serializers.IntegerField()

# Doctor API Serializers

class CreateDoctorApiSerializer(
    serializers.Serializer
):

    name = serializers.CharField()

    email = serializers.EmailField()

    phone_number = serializers.CharField()

    years_of_experience = serializers.IntegerField()

    specialization = serializers.IntegerField()


class UpdateDoctorApiSerializer(
    serializers.Serializer
):

    doctor_id = serializers.IntegerField()

    name = serializers.CharField(
        required=False
    )

    email = serializers.EmailField(
        required=False
    )

    phone_number = serializers.CharField(
        required=False
    )

    years_of_experience = serializers.IntegerField(
        required=False
    )

    specialization = serializers.IntegerField(
        required=False
    )


class GetDoctorDetailsApiSerializer(
    serializers.Serializer
):

    doctor_id = serializers.IntegerField()

class DeleteDoctorApiSerializer(
    serializers.Serializer
):

    doctor_id = serializers.IntegerField()

# Patient API Serializers

class CreatePatientApiSerializer(
    serializers.Serializer
):

    name = serializers.CharField()

    age = serializers.IntegerField()

    gender = serializers.CharField()

    blood_group = serializers.CharField()

    email = serializers.EmailField()

    phone_number = serializers.CharField()


class UpdatePatientApiSerializer(
    serializers.Serializer
):

    patient_id = serializers.IntegerField()

    name = serializers.CharField(
        required=False
    )

    age = serializers.IntegerField(
        required=False
    )

    gender = serializers.CharField(
        required=False
    )

    blood_group = serializers.CharField(
        required=False
    )

    email = serializers.EmailField(
        required=False
    )

    phone_number = serializers.CharField(
        required=False
    )


class GetPatientDetailsApiSerializer(
    serializers.Serializer
):

    patient_id = serializers.IntegerField()

class DeletePatientApiSerializer(
    serializers.Serializer
):

    patient_id = serializers.IntegerField()


# Appointment API Serializers


class CreateAppointmentApiSerializer(
    serializers.Serializer
):

    doctor = serializers.IntegerField()

    patient = serializers.IntegerField()

    appointment_date = serializers.DateField()

    appointment_time = serializers.TimeField()

    symptoms = serializers.CharField()


class UpdateAppointmentApiSerializer(
    serializers.Serializer
):

    appointment_id = serializers.IntegerField()

    appointment_date = serializers.DateField(
        required=False
    )

    appointment_time = serializers.TimeField(
        required=False
    )

    symptoms = serializers.CharField(
        required=False
    )

    status = serializers.CharField(
        required=False
    )


class GetAppointmentDetailsApiSerializer(
    serializers.Serializer
):

    appointment_id = serializers.IntegerField()


class CancelAppointmentApiSerializer(
    serializers.Serializer
):

    appointment_id = serializers.IntegerField()

class CheckDoctorSlotApiSerializer(
    serializers.Serializer
):

    doctor_id = serializers.IntegerField()

    appointment_date = serializers.DateField()

    appointment_time = serializers.TimeField()  
