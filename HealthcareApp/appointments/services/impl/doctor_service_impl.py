import logging

from appointments.dao.impl.doctor_dao_impl import (
    DoctorDAOImpl
)

from appointments.services.interface.doctor_service_interface import (
    DoctorServiceInterface
)

logger = logging.getLogger(__name__)


class DoctorServiceImpl(
    DoctorServiceInterface
):

    def __init__(self):

        self.doctor_dao = DoctorDAOImpl()

    def get_all_doctors(self):

        logger.info(
            "Doctor service: fetching all doctors"
        )

        return self.doctor_dao.get_all_doctors()

    def get_doctor_details(
        self,
        doctor_id
    ):

        logger.info(
            f"Doctor service: fetching doctor {doctor_id}"
        )

        return self.doctor_dao.get_doctor_details(
            doctor_id
        )

    def create_doctor(
        self,
        doctor_data
    ):

        logger.info(
            "Doctor service: creating doctor"
        )

        return self.doctor_dao.create_doctor(
            doctor_data
        )

    def update_doctor(
        self,
        doctor_id,
        doctor_data
    ):

        logger.info(
            f"Doctor service: updating doctor {doctor_id}"
        )

        return self.doctor_dao.update_doctor(
            doctor_id,
            doctor_data
        )

    def delete_doctor(
        self,
        doctor_id
    ):

        logger.info(
            f"Doctor service: deleting doctor {doctor_id}"
        )

        self.doctor_dao.delete_doctor(
            doctor_id
        )