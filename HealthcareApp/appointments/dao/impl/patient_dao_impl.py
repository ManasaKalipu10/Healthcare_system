import logging
import inspect

from appointments.models import Patient
from appointments.dao.interface.patient_dao_interface import (
    PatientDAOInterface
)
from WiseFlow.common.exceptions import (CustomAPIException ,
    PatientNotFoundError
)
logger = logging.getLogger(__name__)


class PatientDAOImpl(PatientDAOInterface):

    def get_all_patients(self):
        """
        Fetch all patients from database.

        Returns:
            QuerySet: List of patient records.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:
            return Patient.objects.all()

        except Exception as e:

            logger.error(
                f"Error fetching patients: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch patients"
            )

    def get_patient_details(self, patient_id):
        """
        Fetches patient details associated with the given patient id.

        Args:
            patient_id (int): The unique identifier of the patient.

        Returns:
            Patient: Patient object if found.

        Raises:
            CustomAPIException:
                If patient is not found or database operation fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            patient = Patient.objects.filter(
                id=patient_id
            ).first()

            if not patient:
                raise PatientNotFoundError(
                     patient_id
                )

            return patient

        except CustomAPIException:
            raise

        except Exception as e:

            logger.error(
                f"Error fetching patient details: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch patient details"
            )

    def create_patient(self, patient_data):
         
        """
         Creates and saves a patient record.

        Args:
            patient_data (dict): Dictionary containing patient information.

        Returns:
            Patient: Newly created patient record.

        Raises:
            CustomAPIException:
                If patient creation fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            return Patient.objects.create(
                **patient_data
            )

        except Exception as e:

            logger.error(
                f"Error creating patient: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to create patient"
            )

    def update_patient(self, patient_id, patient_data):
        """
        Updates patient details for the given patient id.

        Args:
            patient_id (int): The unique identifier of the patient.
            patient_data (dict): Dictionary containing updated patient information.

        Returns:
            Patient: Updated patient record.

        Raises:
            CustomAPIException:
                If patient is not found or update operation fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            patient = Patient.objects.filter(
                id=patient_id
            ).first()

            if not patient:
                raise PatientNotFoundError(
                    patient_id
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

        except CustomAPIException:
            raise

        except Exception as e:

            logger.error(
                f"Error updating patient: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to update patient"
            )

    def delete_patient(self, patient_id):
        """
         Deletes the patient record associated with the given patient id.

        Args:
            patient_id (int): The unique identifier of the patient.

        Raises:
            CustomAPIException:
                If patient is not found or deletion fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            patient = Patient.objects.filter(
                id=patient_id
            ).first()

            if not patient:
                raise PatientNotFoundError(
                    patient_id
                )

            patient.delete()

        except CustomAPIException:
            raise

        except Exception as e:

            logger.error(
                f"Error deleting patient: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to delete patient"
            )