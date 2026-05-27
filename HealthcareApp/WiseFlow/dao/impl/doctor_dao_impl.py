from appointments.models import Doctor

class DoctorDAOImpl:
    def get_all_doctors(self):
        return Doctor.objects.all()
    
    def create_doctor(self, doctor_data):
        doctor = Doctor.objects.create(**doctor_data)
        return doctor   