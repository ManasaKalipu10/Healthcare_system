from abc import ABC, abstractmethod

class SpecializationsDAOInterface(ABC):
    @abstractmethod
    def get_all_specializations(self):
        """
        Fetches all specializations from the database.

        Returns:
            QuerySet: A queryset containing all specialization records.
        
        """
        pass

    @abstractmethod
    def create_specialization(self, specialization_data):
        """Creates a new specialization record in the database.

        Args:
            specialization_data (dict): A dictionary containing the data for the new specialization.

        Returns:
            Specialization: The created specialization object.
        """
        pass

    @abstractmethod
    def get_specialization_details(self, specialization_id):
        """Fetches details of a specific specialization from the database.

        Args:
            specialization_id (int): The ID of the specialization to fetch.

        Returns:
            Specialization: The specialization object with the specified ID.
        """
        pass

    @abstractmethod
    def update_specialization(self, specialization_id, specialization_data):
        """Updates a specific specialization in the database.

        Args:
            specialization_id (int): The ID of the specialization to update.
            specialization_data (dict): A dictionary containing the updated data for the specialization.

        Returns:
            Specialization: The updated specialization object.
        """
        pass

    @abstractmethod
    def delete_specialization(self, specialization_id):
        """Deletes a specific specialization from the database.

        Args:
            specialization_id (int): The ID of the specialization to delete.
        """
        pass