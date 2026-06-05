from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from appointments.models import Specialization
from appointments.tests.test_data.specialization_test_data import (
    SpecializationTestData
)


class BaseTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.specialization = (
            Specialization.objects.create(
                name="Cardiology"
            )
        )


class SpecializationTestCase(BaseTestCase):

    # ==========================================
    # CREATE SPECIALIZATION
    # ==========================================

    def test_create_specialization_success(self):

        payload = (
            SpecializationTestData
            .create_specialization_success_payload
        )

        response = self.client.post(
            reverse("create-specialization"),
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

    def test_create_specialization_invalid(self):

        payload = (
            SpecializationTestData
            .create_specialization_invalid_payload
        )

        response = self.client.post(
            reverse("create-specialization"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # ==========================================
    # GET ALL SPECIALIZATIONS
    # ==========================================

    def test_get_all_specializations_success(self):

        response = self.client.get(
            reverse("get-all-specializations")
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
    # GET SPECIALIZATION DETAILS
    # ==========================================

    def test_get_specialization_details_success(self):

        payload = (
            SpecializationTestData
            .get_specialization_success_payload
        )

        payload["specialization_id"] = (
            self.specialization.id
        )

        response = self.client.post(
            reverse("get-specialization-details"),
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

    def test_get_specialization_details_invalid(self):

        payload = (
            SpecializationTestData
            .get_specialization_invalid_payload
        )

        response = self.client.post(
            reverse("get-specialization-details"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # ==========================================
    # UPDATE SPECIALIZATION
    # ==========================================

    def test_update_specialization_success(self):

        payload = (
            SpecializationTestData
            .update_specialization_success_payload
        )

        payload["specialization_id"] = (
            self.specialization.id
        )

        response = self.client.put(
            reverse("update-specialization"),
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

    def test_update_specialization_invalid(self):

        payload = (
            SpecializationTestData
            .update_specialization_invalid_payload
        )

        response = self.client.put(
            reverse("update-specialization"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # ==========================================
    # DELETE SPECIALIZATION
    # ==========================================

    def test_delete_specialization_success(self):

        payload = (
            SpecializationTestData
            .delete_specialization_success_payload
        )

        payload["specialization_id"] = (
            self.specialization.id
        )

        response = self.client.delete(
            reverse("delete-specialization"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_specialization_invalid(self):

        payload = (
            SpecializationTestData
            .delete_specialization_invalid_payload
        )

        response = self.client.delete(
            reverse("delete-specialization"),
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )