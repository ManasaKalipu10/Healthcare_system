from WiseFlow.services.interface.specializations_service_interface import SpecializationsServiceInterface
from WiseFlow.dao.impl.specializations_dao_impl import SpecializationsDAOImpl

class SpecializationsServiceImpl(SpecializationsServiceInterface):
    def __init__(self):
        self.specializations_dao = SpecializationsDAOImpl()

    def get_all_specializations(self):
        return self.specializations_dao.get_all_specializations()   
    
    def create_specialization(self, specialization_data):
        return self.specializations_dao.create_specialization(specialization_data)  
    
    def get_specialization_details(self, specialization_id):
        return self.specializations_dao.get_specialization_details(specialization_id)   
    
    def update_specialization(self, specialization_id, specialization_data):
        return self.specializations_dao.update_specialization(specialization_id, specialization_data)
    
    def delete_specialization(self, specialization_id):
        return self.specializations_dao.delete_specialization(specialization_id)
    