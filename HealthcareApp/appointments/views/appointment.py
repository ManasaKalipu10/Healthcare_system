import logging
import inspect

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
from WiseFlow.common.custom_response import CustomResponse
from appointments.constants.success_messages import SuccessMessages    
from appointments.serializers import (
    AppointmentSerializer,
    CreateAppointmentApiSerializer,
    UpdateAppointmentApiSerializer,
    GetAppointmentDetailsApiSerializer,
    CancelAppointmentApiSerializer,
    CheckDoctorSlotApiSerializer
)

from appointments.services.impl.appointments_service_impl import (
    AppointmentServiceImpl
)
logger = logging.getLogger(__name__)

class AppointmentViewSet(ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.appointment_service = (
            AppointmentServiceImpl()
        )

    @swagger_auto_schema(
        operation_description="API to fetch all appointments",
        responses={
            status.HTTP_200_OK:
            SuccessMessages.APPOINTMENTS_FETCHED
        }
    )
    @action(detail=False, methods=['get'])
    def get_all_appointments(self, request):
        """
        API endpoint to fetch all appointments.

        This method retrieves all the appointments available in the system. 
        It uses the AppointmentsServiceImpl to fetch the data from the database and 
        returns it in a structured format using the AppointmentSerializer.
        The response includes a success message indicating that the appointments were fetched successfully.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        appointments = (
            self.appointment_service
            .get_all_appointments()
        )

        serializer = AppointmentSerializer(
            appointments,
            many=True
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.APPOINTMENTS_FETCHED,
            status=status.HTTP_200_OK
        ).get_response()
    
    @swagger_auto_schema(
        operation_description="API to create an appointment",
        request_body=CreateAppointmentApiSerializer
    )
    @action(detail=False, methods=['post'])
    def create_appointment(self, request):
        """
        API endpoint to create a new appointment.

        This method allows users to create a new appointment by providing the necessary details in the request body. 
        It uses the AppointmentsServiceImpl to handle the business logic of creating the appointment and 
        returns a success message along with the created appointment details.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        serializer = CreateAppointmentApiSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        appointment_data = serializer.validated_data

        created_appointment = (
            self.appointment_service
            .create_appointment(appointment_data)
        )

        response_serializer = AppointmentSerializer(
            created_appointment
        )

        return CustomResponse(
            data=response_serializer.data,
            message=SuccessMessages.APPOINTMENT_CREATED,
            status=status.HTTP_201_CREATED
        ).get_response()
    
    @swagger_auto_schema(
        operation_description="API to fetch appointment details",
        request_body=GetAppointmentDetailsApiSerializer
    )
    @action(detail=False, methods=['post'])
    def get_appointment_details(self, request):
        """
        API endpoint to fetch appointment details.

        This method retrieves the details of a specific appointment based on the provided appointment ID. 
        It uses the AppointmentsServiceImpl to fetch the data from the database and 
        returns it in a structured format using the AppointmentSerializer.
        The response includes a success message indicating that the appointment details were fetched successfully.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        serializer = GetAppointmentDetailsApiSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        appointment_id = serializer.validated_data.get("appointment_id")

        appointment_details = (
            self.appointment_service
            .get_appointment_details(appointment_id)
        )

        response_serializer = AppointmentSerializer(
            appointment_details
        )

        return CustomResponse(
            data=response_serializer.data,
            message=SuccessMessages.APPOINTMENT_DETAILS_FETCHED,
            status=status.HTTP_200_OK
        ).get_response()
    
    @swagger_auto_schema(
        operation_description="API to update an appointment",
        request_body=UpdateAppointmentApiSerializer
    )
    @action(detail=False, methods=['put'])
    def update_appointment(self, request):  
        """
        API endpoint to update an existing appointment.

        This method allows users to update the details of an existing appointment by providing the necessary information in the request body. 
        It uses the AppointmentsServiceImpl to handle the business logic of updating the appointment and 
        returns a success message along with the updated appointment details.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        serializer = UpdateAppointmentApiSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        appointment_id = serializer.validated_data.get("appointment_id")
        appointment_data = serializer.validated_data

        updated_appointment = (
            self.appointment_service
            .update_appointment(appointment_id, appointment_data)
        )

        response_serializer = AppointmentSerializer(
            updated_appointment
        )

        return CustomResponse(
            data=response_serializer.data,
            message=SuccessMessages.APPOINTMENT_UPDATED,
            status=status.HTTP_200_OK
        ).get_response()
    
    @swagger_auto_schema(
        operation_description="API to cancel an appointment",
        request_body=CancelAppointmentApiSerializer
    )
    @action(detail=False, methods=['post'])
    def cancel_appointment(self, request):  
        """
        API endpoint to cancel an existing appointment.

        This method allows users to cancel an existing appointment by providing the appointment ID in the request body. 
        It uses the AppointmentsServiceImpl to handle the business logic of cancelling the appointment and 
        returns a success message along with the cancelled appointment details.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        serializer = CancelAppointmentApiSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        appointment_id = serializer.validated_data.get("appointment_id")

        cancelled_appointment = (
            self.appointment_service
            .cancel_appointment(appointment_id)
        )

        response_serializer = AppointmentSerializer(
            cancelled_appointment
        )

        return CustomResponse(
            data=response_serializer.data,
            message=SuccessMessages.APPOINTMENT_CANCELLED,
            status=status.HTTP_200_OK
        ).get_response()
    
    @swagger_auto_schema(
        operation_description="API to check doctor availability for a given time slot",
        request_body=CheckDoctorSlotApiSerializer
    )
    @action(detail=False, methods=['post'])
    def check_doctor_slot(self, request):
        """
        API endpoint to check doctor availability for a given time slot.

        This method allows users to check if a doctor is available for a specific date and time slot by providing the necessary information in the request body. 
        It uses the AppointmentsServiceImpl to handle the business logic of checking the doctor's availability and 
        returns a success message along with the availability status.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        serializer = CheckDoctorSlotApiSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        doctor_id = serializer.validated_data.get("doctor_id")
        appointment_date = serializer.validated_data.get("appointment_date")
        appointment_time = serializer.validated_data.get("appointment_time")

        availability_status = (
            self.appointment_service
            .check_doctor_slot(doctor_id, appointment_date, appointment_time)
        )

        return CustomResponse(
            data={"is_available": availability_status},
            message=SuccessMessages.DOCTOR_SLOT_CHECKED,
            status=status.HTTP_200_OK
        ).get_response()