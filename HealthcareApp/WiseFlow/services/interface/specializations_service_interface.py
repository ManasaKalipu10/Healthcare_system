from abc import ABC, abstractmethod

class SpecializationsServiceInterface(ABC):
    @abstractmethod
    def get_all_specializations(self):
        pass

    @abstractmethod
    def create_specialization(self, specialization_data):
        pass

    @abstractmethod
    def get_specialization_details(self, specialization_id):
        pass

    @abstractmethod
    def update_specialization(self, specialization_id, specialization_data):
        pass

    @abstractmethod
    def delete_specialization(self, specialization_id):
        pass