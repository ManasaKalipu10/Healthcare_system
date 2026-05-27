from appointments.models import Specialization 

class SpecializationsDAOImpl:
    def get_all_specializations(self):
        return Specialization.objects.all()
    
    def create_specialization(self, specialization_data):
        specialization = Specialization.objects.create(**specialization_data)
        return specialization