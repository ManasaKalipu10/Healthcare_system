from abc import ABC, abstractmethod

class PatientServiceInterface(ABC):
    @abstractmethod
    def get_all_patients(self):
        """
        Fetches all patients from the database.

        Returns:
            QuerySet: A queryset containing all patient records.
        """
        pass

    @abstractmethod
    def create_patient(self, patient_data):
        """
        Creates a new patient in the database.

        Args:
            patient_data (dict): A dictionary containing the patient's information.

        Returns:
            Patient: The created patient object.
        """
        pass

    @abstractmethod
    def get_patient_details(self, patient_id):
        """
        Fetches details of a specific patient from the database.

        Args:
            patient_id (int): The ID of the patient whose details are to be fetched.

        Returns:
            Patient: The patient object with the specified ID.
        """
        pass

    @abstractmethod
    def update_patient(self, patient_id, patient_data):
        """
        Updates the details of a specific patient in the database.

        Args:
            patient_id (int): The ID of the patient whose details are to be updated.
            patient_data (dict): A dictionary containing the updated patient information.

        Returns:
            Patient: The updated patient object.
        """
        pass

    @abstractmethod
    def delete_patient(self, patient_id):
        """
        Deletes a specific patient from the database.

        Args:
            patient_id (int): The ID of the patient to be deleted.

        Returns:
            bool: True if the patient was deleted, False otherwise.
        """
        pass