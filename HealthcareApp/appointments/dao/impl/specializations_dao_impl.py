import logging
import inspect

from appointments.models import Specialization
from appointments.dao.interface.specializations_dao_interface import (
    SpecializationsDAOInterface
)
from WiseFlow.common.exceptions import (
    CustomAPIException,
    SpecializationNotFoundError
)
                                    

logger = logging.getLogger(__name__)


class SpecializationsDAOImpl(SpecializationsDAOInterface):

    def get_all_specializations(self):
        """
        Fetch all specializations from database.

        Returns:
            QuerySet: List of specialization records.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:
            return Specialization.objects.all()

        except Exception as e:

            logger.error(
                f"Error fetching specializations: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch specializations"
            )

    def get_specialization_details(self, specialization_id):
        """
        Fetches specialization details associated with the given specialization id.

        Args:
            specialization_id (int): The unique identifier of the specialization.

        Returns:
            specialization: specialization object if found.

        Raises:
            CustomAPIException:
                If specialization is not found or database operation fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            specialization = Specialization.objects.filter(
                id=specialization_id
            ).first()

            if not specialization:
                raise SpecializationNotFoundError(
                    specialization_id
                )

            return specialization

        except SpecializationNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error fetching specialization details: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch specialization details"
            )

    def create_specialization(self, specialization_data):
         
        """
         Creates and saves a specialization record.

        Args:
            specialization_data (dict): Dictionary containing specialization information.

        Returns:
            specialization: Newly created specialization record.

        Raises:
            CustomAPIException:
                If specialization creation fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            return Specialization.objects.create(
                **specialization_data
            )

        except Exception as e:

            logger.error(
                f"Error creating specialization: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to create specialization"
            )

    def update_specialization(self, specialization_id, specialization_data):
        """
        Updates specialization details for the given specialization id.

        Args:
            specialization_id (int): The unique identifier of the specialization.
            specialization_data (dict): Dictionary containing updated specialization information.

        Returns:
            specialization: Updated specialization record.

        Raises:
            CustomAPIException:
                If specialization is not found or update operation fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            specialization = Specialization.objects.filter(
                id=specialization_id
            ).first()

            if not specialization:
                raise SpecializationNotFoundError(
                    specialization_id
                )

            for key, value in specialization_data.items():

                if hasattr(specialization, key):
                    setattr(
                        specialization,
                        key,
                        value
                    )

            specialization.save()

            return specialization

        except SpecializationNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error updating specialization: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to update specialization"
            )

    def delete_specialization(self, specialization_id):
        """
         Deletes the specialization record associated with the given specialization id.

        Args:
            specialization_id (int): The unique identifier of the specialization.

        Raises:
            CustomAPIException:
                If specialization is not found or deletion fails.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            specialization = Specialization.objects.filter(
                id=specialization_id
            ).first()

            if not specialization:
                raise SpecializationNotFoundError(
                    specialization_id
                )

            specialization.delete()

        except SpecializationNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error deleting specialization: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to delete specialization"
            )