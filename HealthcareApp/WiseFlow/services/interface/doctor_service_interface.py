from abc import ABC, abstractmethod

class DoctorServiceInterface(ABC):
    @abstractmethod
    def get_all_doctors(self):
        pass

    @abstractmethod
    def create_doctor(self, doctor_data):
        pass

    @abstractmethod
    def get_doctor_details(self, doctor_id):
        pass

    @abstractmethod
    def update_doctor(self, doctor_id, doctor_data):
        pass

    @abstractmethod
    def delete_doctor(self, doctor_id):
        pass