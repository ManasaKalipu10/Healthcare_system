import logging

from appointments.dao.impl.appointments_dao_impl import (
    AppointmentDAOImpl
)   
from appointments.services.interface.appointments_service_interface import (
    AppointmentServiceInterface
)

logger = logging.getLogger(__name__)

class AppointmentServiceImpl(
    AppointmentServiceInterface
):

    def __init__(self):

        self.appointment_dao = AppointmentDAOImpl()

    def get_all_appointments(self):

        logger.info(
            "Appointment service: fetching all appointments"
        )

        return self.appointment_dao.get_all_appointments()

    def create_appointment(
        self,
        appointment_data
    ):

        logger.info(
            "Appointment service: creating appointment"
        )

        return self.appointment_dao.create_appointment(
            appointment_data
        )

    def get_appointment_details(
        self,
        appointment_id
    ):

        logger.info(
            f"Appointment service: fetching appointment {appointment_id}"
        )

        return self.appointment_dao.get_appointment_details(
            appointment_id
        )

    def update_appointment(
        self,
        appointment_id,
        appointment_data
    ):

        logger.info(
            f"Appointment service: updating appointment {appointment_id}"
        )

        return self.appointment_dao.update_appointment(
            appointment_id,
            appointment_data
        )

    def cancel_appointment(
        self,
        appointment_id
    ):

        logger.info(
            f"Appointment service: cancelling appointment {appointment_id}"
        )

        return self.appointment_dao.cancel_appointment(
            appointment_id
        )

    def check_doctor_slot(
        self,
        doctor_id,
        appointment_date,
        appointment_time
    ):

        logger.info(
            f"Appointment service: checking doctor slot for doctor {doctor_id}"
        )

        return self.appointment_dao.check_doctor_slot(
            doctor_id,
            appointment_date,
            appointment_time
        )