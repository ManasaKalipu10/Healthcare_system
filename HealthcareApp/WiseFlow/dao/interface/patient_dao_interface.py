from abc import ABC, abstractmethod

class PatientDAOInterface(ABC):
    @abstractmethod
    def get_all_patients(self):
        pass

    @abstractmethod
    def create_patient(self, patient_data):
        pass

    @abstractmethod
    def get_patient_details(self, patient_id):
        pass

    @abstractmethod
    def update_patient(self, patient_id, patient_data):
        pass

    @abstractmethod
    def delete_patient(self, patient_id):
        pass