import logging

from appointments.models import Appointment
from appointments.dao.interface.appointments_dao_interface import (
    AppointmentDAOInterface
)

logger = logging.getLogger(__name__)

class AppointmentDAOImpl(AppointmentDAOInterface):

    def get_all_appointments(self):

        logger.info(
            "Fetching all appointments from database"
        )

        return Appointment.objects.all()

    def create_appointment(self, appointment_data):

        logger.info(
            "Creating appointment record"
        )

        return Appointment.objects.create(
            **appointment_data
        )

    def get_appointment_details(self, appointment_id):

        logger.info(
            f"Fetching appointment with id: {appointment_id}"
        )

        return Appointment.objects.get(
            id=appointment_id
        )

    def update_appointment(self, appointment_id, appointment_data):

        logger.info(
            f"Updating appointment: {appointment_id}"
        )

        appointment = Appointment.objects.get(
            id=appointment_id
        )

        for key, value in appointment_data.items():

            if hasattr(appointment, key):
                setattr(
                    appointment,
                    key,
                    value
                )

        appointment.save()

    def cancel_appointment(self, appointment_id):

        logger.info(
            f"Cancelling appointment: {appointment_id}"
        )

        appointment = Appointment.objects.get(
            id=appointment_id
        )

        appointment.status = "Cancelled"
        appointment.save()

    def check_doctor_slot(self, doctor_id, appointment_date, appointment_time):

        logger.info(
            f"Checking doctor slot for doctor: {doctor_id} on {appointment_date} at {appointment_time}"
        )

        return Appointment.objects.filter(
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            status="Scheduled"
        ).exists()