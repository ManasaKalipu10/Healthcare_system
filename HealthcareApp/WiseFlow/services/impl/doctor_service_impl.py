from WiseFlow.dao.impl.doctor_dao_impl import DoctorDAOImpl

class DoctorServiceImpl:
    def __init__(self):
        self.doctor_dao = DoctorDAOImpl()
    
    def get_all_doctors(self):
        return self.doctor_dao.get_all_doctors()
    
    def create_doctor(self, doctor_data):
        return self.doctor_dao.create_doctor(doctor_data)