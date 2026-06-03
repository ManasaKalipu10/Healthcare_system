import logging

from appointments.models import Specialization
from appointments.dao.interface.specializations_dao_interface import (
    SpecializationsDAOInterface
)

logger = logging.getLogger(__name__)

class SpecializationsDAOImpl(SpecializationsDAOInterface):
    
    def get_all_specializations(self):

        logger.info(
            "Fetching all specializations from database"
        )

        return Specialization.objects.all()

    def create_specialization(self, specialization_data):

        logger.info(
            "Creating specialization record"
        )

        return Specialization.objects.create(
            **specialization_data
        )

    def get_specialization_details(self, specialization_id):

        logger.info(
            f"Fetching specialization with id: {specialization_id}"
        )

        return Specialization.objects.get(
            id=specialization_id
        )

    def update_specialization(self, specialization_id, specialization_data):

        logger.info(
            f"Updating specialization: {specialization_id}"
        )

        specialization = Specialization.objects.get(
            id=specialization_id
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

    def delete_specialization(self, specialization_id):

        logger.info(
            f"Deleting specialization with id: {specialization_id}"
        )

        specialization = Specialization.objects.get(
            id=specialization_id
        )

        specialization.delete()