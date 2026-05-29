from appointments.models import Doctor

class DoctorDAOImpl:
    def get_all_doctors(self):
        return Doctor.objects.all()
    
    def create_doctor(self, doctor_data):
        doctor = Doctor.objects.create(**doctor_data)
        return doctor   
    
    def get_doctors_by_specialization(self, specialization_name):
        return Doctor.objects.filter(
            specialization__name=specialization_name
        ) 