from appointments.models import Patient
from WiseFlow.dao.interface.patient_dao_interface import PatientDAOInterface

class PatientDAOImpl(PatientDAOInterface):
    
    def get_all_patients(self):
        return Patient.objects.all()
    
    def create_patient(self, patient_data):
        patient = Patient.objects.create(**patient_data)
        return patient
    
    def get_patient_details(self, patient_id):
        return Patient.objects.get(id=patient_id)
    
    def update_patient(self, patient_id, patient_data):
        patient = Patient.objects.get(id=patient_id)
        for key, value in patient_data.items():
            setattr(patient, key, value)
        patient.save()
        return patient
    
    def delete_patient(self, patient_id):
        patient = Patient.objects.get(id=patient_id)
        patient.delete()
        return True