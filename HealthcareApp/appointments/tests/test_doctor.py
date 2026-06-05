import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from appointments.models import Doctor, Specialization
from appointments.tests.test_data.doctor_test_data import (
    DoctorTestData
)


class BaseTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.specialization = (
            Specialization.objects.create(
                name="Cardiology"
            )
        )

        self.doctor = Doctor.objects.create(
            name="Doctor One",
            email="doctor@test.com",
            phone_number="9999999999",
            years_of_experience=5,
            specialization=self.specialization
        )


class DoctorTestCase(BaseTestCase):

    # ==========================================
    # CREATE DOCTOR
    # ==========================================

    def test_create_doctor_success(self):

        payload = (
            DoctorTestData
            .create_doctor_success_payload
        )

        payload["specialization"] = (
            self.specialization.id
        )

        response = self.client.post(
            reverse("create-doctor"),
            payload,
            format="json"
        )
        print("STATUS:", response.status_code)
        print("DATA:", response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertIn(
            "data",
            response.data
        )

    def test_create_doctor_invalid(self):

        payload = (
            DoctorTestData
            .create_doctor_invalid_payload
        )

        response = self.client.post(
            reverse("create-doctor"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # ==========================================
    # GET DOCTOR DETAILS
    # ==========================================

    def test_get_doctor_details_success(self):

        payload = (
            DoctorTestData
            .get_doctor_success_payload
        )

        payload["doctor_id"] = self.doctor.id

        response = self.client.post(
            reverse("get-doctor-details"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "data",
            response.data
        )

    def test_get_doctor_details_invalid(self):

        payload = (
            DoctorTestData
            .get_doctor_invalid_payload
        )

        response = self.client.post(
            reverse("get-doctor-details"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # ==========================================
    # UPDATE DOCTOR
    # ==========================================

    def test_update_doctor_success(self):

        payload = (
            DoctorTestData
            .update_doctor_success_payload
        )

        payload["doctor_id"] = self.doctor.id

        response = self.client.put(
            reverse("update-doctor"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "data",
            response.data
        )

    def test_update_doctor_invalid(self):

        payload = (
            DoctorTestData
            .update_doctor_invalid_payload
        )

        response = self.client.put(
            reverse("update-doctor"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # ==========================================
    # DELETE DOCTOR
    # ==========================================

    def test_delete_doctor_success(self):

        payload = (
            DoctorTestData
            .delete_doctor_success_payload
        )

        payload["doctor_id"] = self.doctor.id

        response = self.client.delete(
            reverse("delete-doctor"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_doctor_invalid(self):

        payload = (
            DoctorTestData
            .delete_doctor_invalid_payload
        )

        response = self.client.delete(
            reverse("delete-doctor"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )