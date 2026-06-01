from appointments.models import Specialization
from WiseFlow.dao.interface.specializations_dao_interface import SpecializationsDAOInterface

class SpecializationsDAOImpl(SpecializationsDAOInterface):
    def get_all_specializations(self):
        return Specialization.objects.all()
    
    def create_specialization(self, specialization_data):
        specialization = Specialization.objects.create(**specialization_data)
        return specialization
    
    def get_specialization_details(self, specialization_id):
        return Specialization.objects.get(id=specialization_id)
    
    def update_specialization(self, specialization_id, specialization_data):
        specialization = Specialization.objects.get(id=specialization_id)
        for key, value in specialization_data.items():
            setattr(specialization, key, value)
        specialization.save()
        return specialization
    
    def delete_specialization(self, specialization_id):
        specialization = Specialization.objects.get(id=specialization_id)
        specialization.delete()
        return True