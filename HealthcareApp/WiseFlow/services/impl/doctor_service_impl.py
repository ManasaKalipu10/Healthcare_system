from WiseFlow.services.interface.doctor_service_interface import DoctorServiceInterface
from WiseFlow.dao.impl.doctor_dao_impl import DoctorDAOImpl

class DoctorServiceImpl(DoctorServiceInterface):
    def __init__(self):
        self.doctor_dao = DoctorDAOImpl()

    def get_all_doctors(self):
        return self.doctor_dao.get_all_doctors()

    def create_doctor(self, doctor_data):
        return self.doctor_dao.create_doctor(doctor_data)

    def get_doctor_details(self, doctor_id):
        return self.doctor_dao.get_doctor_details(doctor_id)

    def update_doctor(self, doctor_id, doctor_data):
        return self.doctor_dao.update_doctor(doctor_id, doctor_data)

    def delete_doctor(self, doctor_id):
        return self.doctor_dao.delete_doctor(doctor_id)