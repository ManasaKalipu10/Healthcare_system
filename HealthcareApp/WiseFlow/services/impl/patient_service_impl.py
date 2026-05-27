from WiseFlow.dao.impl.patient_dao_impl import PatientDAOImpl   
class PatientServiceImpl:
    def __init__(self):
        self.patient_dao = PatientDAOImpl()
    
    def get_all_patients(self):
        return self.patient_dao.get_all_patients()
    
    def create_patient(self, patient_data):
        return self.patient_dao.create_patient(patient_data)