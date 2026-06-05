from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    years_of_experience = models.IntegerField()

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Patient(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    blood_group = models.CharField(max_length=5)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField(default="10:00")

    symptoms = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def full_clean(self):

        # prevent previous date booking
        if self.appointment_date < date.today():
            raise ValidationError(
                "Previous dates are not allowed."
            )

        # check doctor availability
        existing_appointment = Appointment.objects.filter(
            doctor=self.doctor,
            appointment_date=self.appointment_date,
            appointment_time=self.appointment_time
        ).exclude(id=self.id)

        if existing_appointment.exists():
            raise ValidationError(
                "Doctor already has appointment at this time."
            )

    def __str__(self):
        return (
            f"{self.patient.name} - "
            f"{self.doctor.name} - "
            f"{self.appointment_date}"
        )