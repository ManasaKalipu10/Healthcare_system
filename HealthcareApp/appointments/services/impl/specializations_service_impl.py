import logging

from appointments.dao.impl.specializations_dao_impl import (
    SpecializationsDAOImpl
)

from appointments.services.interface.specializations_service_interface import (
    SpecializationsServiceInterface
)

from WiseFlow.common.exceptions import (
    SpecializationNotFoundError
)

logger = logging.getLogger(__name__)


class SpecializationServiceImpl(
    SpecializationsServiceInterface
):

    def init__(self):

        self.specialization_dao = SpecializationsDAOImpl()  

    def get_all_specializations(self):

        logger.info(
            "Specialization service: fetching all specializations"
        )

        return self.specialization_dao.get_all_specializations()    
    
    def create_specialization(
        self,
        specialization_data
    ):

        logger.info(
            "Specialization service: creating specialization"
        )

        return self.specialization_dao.create_specialization(
            specialization_data
        )
    def get_specialization_details(
        self,
        specialization_id
    ):

        logger.info(
            f"Specialization service: fetching specialization {specialization_id}"
        )

        specialization = self.specialization_dao.get_specialization_details(
            specialization_id
        )

        if not specialization:
            raise SpecializationNotFoundError(
                f"Specialization with id {specialization_id} not found"
            )

        return specialization   
    
    def update_specialization(
        self,
        specialization_id,
        specialization_data
    ):

        logger.info(
            f"Specialization service: updating specialization {specialization_id}"
        )

        specialization = self.specialization_dao.update_specialization(
            specialization_id,
            specialization_data
        )

        if not specialization:
            raise SpecializationNotFoundError(
                f"Specialization with id {specialization_id} not found"
            )

        return specialization
    
    def delete_specialization(  
        self,
        specialization_id
    ):

        logger.info(
            f"Specialization service: deleting specialization {specialization_id}"
        )

        specialization = self.specialization_dao.delete_specialization(
            specialization_id
        )

        if not specialization:
            raise SpecializationNotFoundError(
                f"Specialization with id {specialization_id} not found"
            )
        return specialization