import logging

from appointments.models import Patient
from appointments.dao.interface.patient_dao_interface import (
    PatientDAOInterface
)

logger = logging.getLogger(__name__)

class PatientDAOImpl(PatientDAOInterface):

    def get_all_patients(self):

        logger.info(
            "Fetching all patients from database"
        )

        return Patient.objects.all()

    def create_patient(self, patient_data):

        logger.info(
            "Creating patient record"
        )

        return Patient.objects.create(
            **patient_data
        )

    def get_patient_details(self, patient_id):

        logger.info(
            f"Fetching patient with id: {patient_id}"
        )

        return Patient.objects.get(
            id=patient_id
        )

    def update_patient(self, patient_id, patient_data):

        logger.info(
            f"Updating patient: {patient_id}"
        )

        patient = Patient.objects.get(
            id=patient_id
        )

        for key, value in patient_data.items():

            if hasattr(patient, key):
                setattr(
                    patient,
                    key,
                    value
                )

        patient.save()

        return patient

    def delete_patient(self, patient_id):

        logger.info(
            f"Deleting patient: {patient_id}"
        )

        patient = Patient.objects.get(
            id=patient_id
        )

        patient.delete()