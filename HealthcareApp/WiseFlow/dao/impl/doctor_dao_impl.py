from appointments.models import Doctor
from WiseFlow.dao.interface.doctor_dao_interface import DoctorDAOInterface

class DoctorDAOImpl(DoctorDAOInterface):

    def get_all_doctors(self):
        return Doctor.objects.all()
    
    def create_doctor(self, doctor_data):
        doctor = Doctor.objects.create(**doctor_data)
        return doctor
    
    def get_doctor_details(self, doctor_id):
        return Doctor.objects.get(id=doctor_id)
    
    def update_doctor(self, doctor_id, doctor_data):
        doctor = Doctor.objects.get(id=doctor_id)
        for key, value in doctor_data.items():
            setattr(doctor, key, value)
        doctor.save()
        return doctor
    
    def delete_doctor(self, doctor_id):
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.delete()
        return True