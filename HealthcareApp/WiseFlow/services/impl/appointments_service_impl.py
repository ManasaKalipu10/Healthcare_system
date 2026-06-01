from datetime import datetime, date

from WiseFlow.services.interface.appointments_service_interface import AppointmentServiceInterface
from WiseFlow.dao.impl.appointments_dao_impl import AppointmentDAOImpl


class AppointmentServiceImpl(AppointmentServiceInterface):

    def __init__(self):
        self.appointment_dao = AppointmentDAOImpl()

    def get_all_appointments(self):
        return self.appointment_dao.get_all_appointments()

    def get_appointment_details(self, appointment_id):
        return self.appointment_dao.get_appointment_details(
            appointment_id
        )

    def create_appointment(self, appointment_data):

        appointment_date = datetime.strptime(
            appointment_data["appointment_date"],
            "%Y-%m-%d"
        ).date()

        if appointment_date < date.today():
            raise Exception(
                "Past appointments are not allowed"
            )

        doctor_exists = self.appointment_dao.check_doctor_slot(
            appointment_data["doctor"],
            appointment_data["appointment_date"],
            appointment_data["appointment_time"]
        )

        if doctor_exists:
            raise Exception(
                "Doctor already has appointment in this slot"
            )

        return self.appointment_dao.create_appointment(
            appointment_data
        )

    def update_appointment(
        self,
        appointment_id,
        appointment_data
    ):
        return self.appointment_dao.update_appointment(
            appointment_id,
            appointment_data
        )

    def cancel_appointment(self, appointment_id):
        self.appointment_dao.cancel_appointment(
            appointment_id
        )

    def check_doctor_slot(
        self,
        doctor_id,
        appointment_date,
        appointment_time
    ):
        return self.appointment_dao.check_doctor_slot(
            doctor_id,
            appointment_date,
            appointment_time
        )