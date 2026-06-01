from abc import ABC, abstractmethod

class AppointmentServiceInterface(ABC):
    @abstractmethod
    def get_all_appointments(self):
        pass

    @abstractmethod
    def create_appointment(self, appointment_data):
        pass

    @abstractmethod
    def get_appointment_details(self, appointment_id):
        pass

    @abstractmethod
    def update_appointment(self, appointment_id, appointment_data):
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id):
        pass
        
    @abstractmethod
    def check_doctor_slot(self, doctor_id, appointment_date, appointment_time):
        pass