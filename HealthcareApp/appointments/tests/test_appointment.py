import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from appointments.models import Doctor, Patient, Specialization
from appointments.tests.test_data.appointment_test_data import AppointmentTestData


class BaseTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.specialization = Specialization.objects.create(
            name="Cardiology"
        )

        self.doctor = Doctor.objects.create(
            name="Doctor One",
            email="doctor@test.com",
            phone_number="9999999999",
            years_of_experience=5,
            specialization=self.specialization
        )

        self.patient = Patient.objects.create(
            name="Patient One",
            age=30,
            gender="Male",
            blood_group="O+",
            email="patient@test.com",
            phone_number="8888888888"
        )


class AppointmentTestCase(BaseTestCase):

    # =====================================================
    # CREATE APPOINTMENT API
    # =====================================================

    # 1. With all correct values
    def test_create_appointment_success(self):

        payload = AppointmentTestData.create_appointment_success_payload
        payload["doctor"] = self.doctor.id
        payload["patient"] = self.patient.id

        response = self.client.post(
            reverse("create-appointment"),
            payload,
            format="json"
        )
        
        print("STATUS:", response.status_code)
        print("DATA:", response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("data", response.data)


    # 2. With invalid payload
    def test_create_appointment_invalid(self):

        payload = AppointmentTestData.create_appointment_invalid_payload

        response = self.client.post(
            reverse("create-appointment"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertDictEqual(
            json.loads(response.content),
            AppointmentTestData.create_appointment_invalid_response
        )

    # =====================================================
    # GET APPOINTMENT DETAILS API
    # =====================================================

    # 1. With all correct values
    def test_get_appointment_details_success(self):

        create_payload = {
            "doctor": self.doctor.id,
            "patient": self.patient.id,
            "appointment_date": "2026-06-10",
            "appointment_time": "10:00:00",
            "symptoms": "Fever"
        }

        create_res = self.client.post(
            reverse("create-appointment"),
            create_payload,
            format="json"
        )

        appointment_id = create_res.data.get("data", {}).get("id")


        print(f"Appointment ID: {appointment_id or 'None'}")


        payload = AppointmentTestData.get_appointment_success_payload
        payload["appointment_id"] = appointment_id

        response = self.client.post(
            reverse("get-appointment-details"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.data)

    # 2. With invalid payload
    def test_get_appointment_details_invalid(self):

        payload = AppointmentTestData.get_appointment_invalid_payload

        response = self.client.post(
            reverse("get-appointment-details"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # =====================================================
    # UPDATE APPOINTMENT API
    # =====================================================

    # 1. With all correct values
    def test_update_appointment_success(self):

        create_payload = {
            "doctor": self.doctor.id,
            "patient": self.patient.id,
            "appointment_date": "2026-06-10",
            "appointment_time": "10:00:00",
            "symptoms": "Fever"
        }

        create_res = self.client.post(
            reverse("create-appointment"),
            create_payload,
            format="json"
        )

        appointment_id = create_res.data.get("data", {}).get("id")


        print(f"Appointment ID: {appointment_id or 'None'}")


        payload = AppointmentTestData.update_appointment_success_payload
        payload["appointment_id"] = appointment_id

        response = self.client.put(
            reverse("update-appointment"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.data)

    # 2. With invalid payload
    def test_update_appointment_invalid(self):

        payload = AppointmentTestData.update_appointment_invalid_payload

        response = self.client.put(
            reverse("update-appointment"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # =====================================================
    # CANCEL APPOINTMENT API
    # =====================================================

    # 1. With all correct values
    def test_cancel_appointment_success(self):

        create_payload = {
            "doctor": self.doctor.id,
            "patient": self.patient.id,
            "appointment_date": "2026-06-10",
            "appointment_time": "10:00:00",
            "symptoms": "Fever"
        }

        create_res = self.client.post(
            reverse("create-appointment"),
            create_payload,
            format="json"
        )

        appointment_id = create_res.data.get("data", {}).get("id")


        print(f"Appointment ID: {appointment_id or 'None'}")


        payload = AppointmentTestData.cancel_appointment_success_payload
        payload["appointment_id"] = appointment_id

        response = self.client.post(
            reverse("cancel-appointment"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.data)

    # 2. With invalid payload
    def test_cancel_appointment_invalid(self):

        payload = AppointmentTestData.cancel_appointment_invalid_payload

        response = self.client.post(
            reverse("cancel-appointment"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # =====================================================
    # CHECK DOCTOR SLOT API
    # =====================================================

    # 1. With all correct values
    def test_check_doctor_slot_success(self):

        payload = AppointmentTestData.check_slot_success_payload
        payload["doctor_id"] = self.doctor.id

        response = self.client.post(
            reverse("check-doctor-slot"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.data)

    # 2. With invalid payload
    def test_check_doctor_slot_invalid(self):

        payload = AppointmentTestData.check_slot_invalid_payload

        response = self.client.post(
            reverse("check-doctor-slot"),
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)