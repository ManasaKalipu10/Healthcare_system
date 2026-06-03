import logging

from appointments.models import Doctor
from appointments.dao.interface.doctor_dao_interface import (
    DoctorDAOInterface
)

logger = logging.getLogger(__name__)


class DoctorDAOImpl(DoctorDAOInterface):

    def get_all_doctors(self):

        logger.info(
            "Fetching all doctors from database"
        )

        return Doctor.objects.all()

    def get_doctor_details(self, doctor_id):

        logger.info(
            f"Fetching doctor with id: {doctor_id}"
        )

        return Doctor.objects.get(
            id=doctor_id
        )

    def create_doctor(self, doctor_data):

        logger.info(
            "Creating doctor record"
        )

        return Doctor.objects.create(
            **doctor_data
        )

    def update_doctor(
        self,
        doctor_id,
        doctor_data
    ):

        logger.info(
            f"Updating doctor: {doctor_id}"
        )

        doctor = Doctor.objects.get(
            id=doctor_id
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

    def delete_doctor(self, doctor_id):

        logger.info(
            f"Deleting doctor: {doctor_id}"
        )

        doctor = Doctor.objects.get(
            id=doctor_id
        )

        doctor.delete()