from appointments.models import Appointment


class AppointmentDAOImpl:

    def get_all_appointments(self):
        return Appointment.objects.all()

    def create_appointment(self, appointment_data):
        appointment = Appointment.objects.create(**appointment_data)
        return appointment

    def check_doctor_availability(self, doctor, appointment_date, appointment_time):

        return Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()