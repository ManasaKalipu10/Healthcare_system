from WiseFlow.dao.impl.appointment_dao_impl import AppointmentDAOImpl


class AppointmentServiceImpl:

    def __init__(self):
        self.appointment_dao = AppointmentDAOImpl()

    def get_all_appointments(self):
        return self.appointment_dao.get_all_appointments()

    def create_appointment(self, appointment_data):
        return self.appointment_dao.create_appointment(appointment_data)

    def check_doctor_availability(self, doctor, appointment_date, appointment_time):

        return self.appointment_dao.check_doctor_availability(
            doctor,
            appointment_date,
            appointment_time
        )