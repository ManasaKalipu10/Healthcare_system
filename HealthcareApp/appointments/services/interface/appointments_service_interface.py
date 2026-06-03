from abc import ABC, abstractmethod

class AppointmentServiceInterface(ABC):
    @abstractmethod
    def get_all_appointments(self):
        """
        Fetches all appointments from the database.

        Returns:
            QuerySet: A queryset containing all appointment records.

        """
        pass

    @abstractmethod
    def create_appointment(self, appointment_data):
        """
        Creates a new appointment record in the database.

        Args:
            appointment_data (dict): A dictionary containing the appointment information.

        Returns:
            Appointment: The created appointment instance.
        """
        pass

    @abstractmethod
    def get_appointment_details(self, appointment_id):
        """
        Fetches the details of a specific appointment.

        Args:
            appointment_id (int): The ID of the appointment to fetch.

        Returns:
            Appointment: The appointment instance with the specified ID.
        """
        pass

    @abstractmethod
    def update_appointment(self, appointment_id, appointment_data):
        """
        Updates an existing appointment record in the database.

        Args:
            appointment_id (int): The ID of the appointment to update.
            appointment_data (dict): A dictionary containing the updated appointment information.

        Returns:
            Appointment: The updated appointment instance.
        """
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id):
        """
        Cancels an existing appointment record in the database.

        Args:
            appointment_id (int): The ID of the appointment to cancel.

        Returns:
            Appointment: The cancelled appointment instance.
        """
        pass
        
    @abstractmethod
    def check_doctor_slot(self, doctor_id, appointment_date, appointment_time):
        """
        Checks if a doctor has an available slot for a given date and time.

        Args:
            doctor_id (int): The ID of the doctor to check.
            appointment_date (date): The date of the appointment.
            appointment_time (time): The time of the appointment.

        Returns:
            bool: True if the slot is available, False otherwise.
        """
        pass