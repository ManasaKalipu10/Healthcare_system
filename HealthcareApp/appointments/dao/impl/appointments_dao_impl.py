import logging
import inspect

from appointments.models import Appointment
from appointments.dao.interface.appointments_dao_interface import (
    AppointmentDAOInterface
)
from WiseFlow.common.exceptions import (
    CustomAPIException,
    AppointmentNotFoundError
)

logger = logging.getLogger(__name__)


class AppointmentDAOImpl(AppointmentDAOInterface):

    def get_all_appointments(self):
        """
        Fetch all appointments from database.

        Returns:
            QuerySet: List of appointment records.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:
            return Appointment.objects.all()

        except Exception as e:

            logger.error(
                f"Error fetching appointments: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch appointments"
            )

    def create_appointment(self, appointment_data):
        """
        Create a new appointment record.

        Args:
            appointment_data (dict): Appointment details.

        Returns:
            Appointment: Created appointment object.
        """

        logger.info(
        f"Entering {self.__class__.__name__} :: "
        f"{inspect.currentframe().f_code.co_name}"
    )

        try:
            appointment = Appointment(**appointment_data)

            appointment.full_clean()

            appointment.save()

            return appointment

        except Exception as e:
            print("ERROR TYPE:", type(e))
            print("ERROR:", repr(e))
            raise
        

    def get_appointment_details(self, appointment_id):
        """
        Fetch appointment details by id.

        Args:
            appointment_id (int): Appointment id.

        Returns:
            Appointment: Appointment object.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            appointment = Appointment.objects.filter(
                id=appointment_id
            ).first()

            if not appointment:
                raise AppointmentNotFoundError(appointment_id)

            return appointment

        except AppointmentNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error fetching appointment details: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to fetch appointment details"
            )

    def update_appointment(
        self,
        appointment_id,
        appointment_data
    ):
        """
        Update appointment details.

        Args:
            appointment_id (int): Appointment id.
            appointment_data (dict): Updated appointment data.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            appointment = Appointment.objects.filter(
                id=appointment_id
            ).first()

            if not appointment:
                raise AppointmentNotFoundError(appointment_id)

            allowed_fields = {
                "appointment_date",
                "appointment_time",
                "status",
                "symptoms"
            }

            for field, value in appointment_data.items():

                if field in allowed_fields:
                    setattr(
                        appointment,
                        field,
                        value
                    )

            appointment.save()

            return appointment

        except AppointmentNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error updating appointment: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to update appointment"
            )

    def cancel_appointment(self, appointment_id):
        """
        Cancel an appointment.

        Args:
            appointment_id (int): Appointment id.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            appointment = Appointment.objects.filter(
                id=appointment_id
            ).first()

            if not appointment:
                raise AppointmentNotFoundError(appointment_id)

            appointment.status = "Cancelled"
            appointment.save()

            return appointment

        except AppointmentNotFoundError:
            raise

        except Exception as e:

            logger.error(
                f"Error cancelling appointment: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to cancel appointment"
            )

    def check_doctor_slot(
        self,
        doctor_id,
        appointment_date,
        appointment_time
    ):
       
        """
        Check whether a doctor's slot is already booked.

        Args:
            doctor_id (int): Doctor id.
            appointment_date (date): Appointment date.
            appointment_time (time): Appointment time.

        Returns:
            bool: True if slot exists, else False.
        """

        logger.info(
            f"Entering {self.__class__.__name__} :: "
            f"{inspect.currentframe().f_code.co_name}"
        )

        try:

            return Appointment.objects.filter(
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                status__in=["Pending", "Confirmed"]
            ).exists()

        except Exception as e:

            logger.error(
                f"Error checking doctor slot: {str(e)}"
            )

            raise CustomAPIException(
                "Unable to check doctor availability"
            )
        
       