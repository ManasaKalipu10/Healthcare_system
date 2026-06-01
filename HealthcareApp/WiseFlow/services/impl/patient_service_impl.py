from WiseFlow.services.interface.patient_service_interface import PatientServiceInterface
from WiseFlow.dao.impl.patient_dao_impl import PatientDAOImpl

class PatientServiceImpl(PatientServiceInterface):
    def __init__(self):
        self.patient_dao = PatientDAOImpl()

    def get_all_patients(self):
        return self.patient_dao.get_all_patients()

    def create_patient(self, patient_data):
        return self.patient_dao.create_patient(patient_data)

    def get_patient_details(self, patient_id):
        return self.patient_dao.get_patient_details(patient_id)

    def update_patient(self, patient_id, patient_data):
        return self.patient_dao.update_patient(patient_id, patient_data)

    def delete_patient(self, patient_id):
        return self.patient_dao.delete_patient(patient_id)