import logging
import inspect

from appointments.models import Doctor
from appointments.dao.interface.doctor_dao_interface import (
    DoctorDAOInterface
)
from WiseFlow.common.exceptions import (
    CustomAPIException,
    DoctorNotFoundError
)

logger = logging.getLogger(__name__)


class DoctorDAOImpl(DoctorDAOInterface):

    def get_all_doctors(self):
        """
        Fetch all doctors from database.

        Returns:
            QuerySet: List of doctor records.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:
            return Doctor.objects.all()

        except Exception as e:

            logger.error(
                f"Error fetching doctors: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch doctors"
            )

    def get_doctor_details(self, doctor_id):
        """
        Fetch doctor details by id.

        Args:
            doctor_id (int): Doctor identifier.

        Returns:
            Doctor: Doctor object.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            doctor = Doctor.objects.filter(
                id=doctor_id
            ).first()

            if not doctor:
                raise DoctorNotFoundError(
                    doctor_id
                )

            return doctor

        except DoctorNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error fetching doctor details: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch doctor details"
            )

    def create_doctor(self, doctor_data):
        """
        Create a doctor record.

        Args:
            doctor_data (dict): Doctor information.

        Returns:
            Doctor: Created doctor object.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            return Doctor.objects.create(
                **doctor_data
            )

        except Exception as e:

            logger.error(
                f"Error creating doctor: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to create doctor"
            )

    def update_doctor(
        self,
        doctor_id,
        doctor_data
    ):
        """
        Update doctor details.

        Args:
            doctor_id (int): Doctor identifier.
            doctor_data (dict): Updated doctor information.

        Returns:
            Doctor: Updated doctor object.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            doctor = Doctor.objects.filter(
                id=doctor_id
            ).first()

            if not doctor:
                raise DoctorNotFoundError(
                    doctor_id
                )

            for key, value in doctor_data.items():

                if hasattr(doctor, key):
                    setattr(
                        doctor,
                        key,
                        value
                    )

            doctor.save()

            return doctor

        except DoctorNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error updating doctor: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to update doctor"
            )

    def delete_doctor(self, doctor_id):
        """
        Delete doctor record.

        Args:
            doctor_id (int): Doctor identifier.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            doctor = Doctor.objects.filter(
                id=doctor_id
            ).first()

            if not doctor:
                raise DoctorNotFoundError(
                    doctor_id
                )

            doctor.delete()

        except DoctorNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error deleting doctor: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to delete doctor"
            )