from appointments.models import Appointment
from WiseFlow.dao.interface.appointments_dao_interface import AppointmentDAOInterface

class AppointmentDAOImpl(AppointmentDAOInterface):

    def get_all_appointments(self):
        return Appointment.objects.all()

    def get_appointment_details(self, appointment_id):
        return Appointment.objects.get(id=appointment_id)

    def create_appointment(self, appointment_data):
        return Appointment.objects.create(**appointment_data)

    def update_appointment(self, appointment_id, appointment_data):

        appointment = Appointment.objects.get(id=appointment_id)

        for key, value in appointment_data.items():
            setattr(appointment, key, value)

        appointment.save()

        return appointment

    def cancel_appointment(self, appointment_id):

        appointment = Appointment.objects.get(id=appointment_id)

        appointment.delete()

    def check_doctor_slot(
        self,
        doctor_id,
        appointment_date,
        appointment_time
    ):

        return Appointment.objects.filter(
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()