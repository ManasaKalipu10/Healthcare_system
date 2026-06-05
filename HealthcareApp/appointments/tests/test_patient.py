from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from appointments.models import Patient
from appointments.tests.test_data.patient_test_data import (
    PatientTestData
)


class BaseTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.patient = Patient.objects.create(
            name="Patient One",
            age=25,
            gender="Male",
            blood_group="O+",
            email="patient@test.com",
            phone_number="9999999999"
        )


class PatientTestCase(BaseTestCase):

    # ==========================================
    # CREATE PATIENT
    # ==========================================

    def test_create_patient_success(self):

        payload = (
            PatientTestData
            .create_patient_success_payload
        )

        response = self.client.post(
            reverse("create-patient"),
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

    def test_create_patient_invalid(self):

        payload = (
            PatientTestData
            .create_patient_invalid_payload
        )

        response = self.client.post(
            reverse("create-patient"),
            payload,
            format="json"
        )
        print(response.status_code)
        print(response.data)

        self.assertEqual(
            response.status_code,
             status.HTTP_400_BAD_REQUEST
        )

    # ==========================================
    # GET ALL PATIENTS
    # ==========================================

    def test_get_all_patients_success(self):

        response = self.client.get(
            reverse("get-all-patients")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "data",
            response.data
        )

    # ==========================================
    # GET PATIENT DETAILS
    # ==========================================

    def test_get_patient_details_success(self):

        payload = (
            PatientTestData
            .get_patient_success_payload
        )

        payload["patient_id"] = (
            self.patient.id
        )

        response = self.client.post(
            reverse("get-patient-details"),
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

    def test_get_patient_details_invalid(self):

        payload = (
            PatientTestData
            .get_patient_invalid_payload
        )

        response = self.client.post(
            reverse("get-patient-details"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
             status.HTTP_404_NOT_FOUND
        )

    # ==========================================
    # UPDATE PATIENT
    # ==========================================

    def test_update_patient_success(self):

        payload = (
            PatientTestData
            .update_patient_success_payload
        )

        payload["patient_id"] = (
            self.patient.id
        )

        response = self.client.put(
            reverse("update-patient"),
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

    def test_update_patient_invalid(self):

        payload = (
            PatientTestData
            .update_patient_invalid_payload
        )

        response = self.client.put(
            reverse("update-patient"),
            payload,
            format="json"
        )
        print(response.status_code)
        print(response.data)

        self.assertEqual(
            response.status_code,
             status.HTTP_404_NOT_FOUND
        )

    # ==========================================
    # DELETE PATIENT
    # ==========================================

    def test_delete_patient_success(self):

        payload = (
            PatientTestData
            .delete_patient_success_payload
        )

        payload["patient_id"] = (
            self.patient.id
        )

        response = self.client.delete(
            reverse("delete-patient"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_patient_invalid(self):

        payload = (
            PatientTestData
            .delete_patient_invalid_payload
        )

        response = self.client.delete(
            reverse("delete-patient"),
            payload,
            format="json"
        )
        
 
        self.assertEqual(
            response.status_code,
             status.HTTP_404_NOT_FOUND
        )