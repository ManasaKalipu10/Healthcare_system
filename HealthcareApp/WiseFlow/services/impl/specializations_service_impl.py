from WiseFlow.dao.impl.specializations_dao_impl import SpecializationsDAOImpl
class SpecializationsServiceImpl:
    def __init__(self):
        self.specializations_dao = SpecializationsDAOImpl()
    
    def get_all_specializations(self):
        return self.specializations_dao.get_all_specializations()
    
    def create_specialization(self, specialization_data):
        return self.specializations_dao.create_specialization(specialization_data)