from abc import ABC, abstractmethod

class DoctorDAOInterface(ABC):
    @abstractmethod
    def get_all_doctors(self):
        """
        Fetches all doctors from the database.

        Returns:
            QuerySet: A queryset containing all doctor records.
        """
        pass

    @abstractmethod
    def create_doctor(self, doctor_data):
        """
        Creates a new doctor record in the database.

        Args:
            doctor_data (dict): A dictionary containing the doctor's information.

        Returns:
            Doctor: The created doctor instance.
        """
        pass

    @abstractmethod
    def get_doctor_details(self, doctor_id):
        """
        Fetches details of a specific doctor from the database.

        Args:
            doctor_id (int): The ID of the doctor whose details are to be fetched.

        Returns:
            Doctor: The doctor instance with the specified ID.
        """
        pass

    @abstractmethod
    def update_doctor(self, doctor_id, doctor_data):
        """
        Updates the details of an existing doctor in the database.

        Args:
            doctor_id (int): The ID of the doctor whose details are to be updated.
            doctor_data (dict): A dictionary containing the updated doctor information.

        Returns:
            Doctor: The updated doctor instance.
        """
        pass

    @abstractmethod
    def delete_doctor(self, doctor_id):
        """
        Deletes a doctor record from the database.

        Args:
            doctor_id (int): The ID of the doctor to be deleted.
        """
        pass