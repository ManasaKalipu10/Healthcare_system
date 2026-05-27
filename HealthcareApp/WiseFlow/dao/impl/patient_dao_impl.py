from appointments.models import Patient

class PatientDAOImpl:
    def get_all_patients(self):
        return Patient.objects.all()
    
    def create_patient(self, patient_data):
        patient = Patient.objects.create(**patient_data)
        return patient