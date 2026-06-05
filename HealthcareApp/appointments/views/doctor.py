import logging
import inspect

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from WiseFlow.common.custom_response import CustomResponse
from appointments.constants.success_messages import SuccessMessages

from appointments.serializers import (
    DoctorSerializer,
    CreateDoctorApiSerializer,
    UpdateDoctorApiSerializer,
    GetDoctorDetailsApiSerializer,
    DeleteDoctorApiSerializer
)

from appointments.services.impl.doctor_service_impl import (
    DoctorServiceImpl
)

logger = logging.getLogger(__name__)


class DoctorViewSet(ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doctor_service = DoctorServiceImpl()

    @swagger_auto_schema(
        operation_description="API to fetch all doctors",
        responses={
            status.HTTP_200_OK:
            SuccessMessages.DOCTORS_FETCHED
        }
    )
    @action(detail=False, methods=['get'])
    def get_all_doctors(self, request):
        """
        API endpoint to fetch all doctors.

        This method retrieves all the doctors available in the system. 
        It uses the DoctorServiceImpl to fetch the data from the database and 
        returns it in a structured format using the DoctorSerializer.
        The response includes a success message indicating that the doctors were fetched successfully.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        doctors = self.doctor_service.get_all_doctors()

        serializer = DoctorSerializer(
            doctors,
            many=True
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.DOCTORS_FETCHED,
            status_code=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        operation_description="API to fetch doctor details",
        request_body=GetDoctorDetailsApiSerializer
    )
    @action(detail=False, methods=['post'])
    def get_doctor_details(self, request):
        """
        API endpoint to fetch doctor details.

        This method retrieves the details of a specific doctor based on the provided doctor ID. 
        It uses the DoctorServiceImpl to fetch the data from the database and 
        returns it in a structured format using the DoctorSerializer.
        The response includes a success message indicating that the doctor details were fetched successfully.   

        """

        doctor_id = request.data.get("doctor_id")

        doctor = (
            self.doctor_service
            .get_doctor_details(doctor_id)
        )

        serializer = DoctorSerializer(
            doctor
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.DOCTOR_DETAILS_FETCHED,
            status_code=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        operation_description="API to create doctor",
        request_body=CreateDoctorApiSerializer
    )
    @action(detail=False, methods=['post'])
    def create_doctor(self, request):

        print("STEP 1")

        serializer = CreateDoctorApiSerializer(
            data=request.data
        )

        print("STEP 2")

        serializer.is_valid(raise_exception=True)

        print("STEP 3", serializer.validated_data)

        doctor = self.doctor_service.create_doctor(
            serializer.validated_data
        )

        print("STEP 4", doctor)

        response_serializer = DoctorSerializer(
            doctor
        )

        print("STEP 5", response_serializer.data)

        return CustomResponse(
            data=response_serializer.data,
            message=SuccessMessages.DOCTOR_CREATED,
            status_code=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        operation_description="API to update doctor",
        request_body=UpdateDoctorApiSerializer
    )
    @action(detail=False, methods=['put'])
    def update_doctor(self, request):
        """
        API endpoint to update doctor.
        """

        doctor_id = request.data.get(
            "doctor_id"
        )

        doctor = (
            self.doctor_service
            .update_doctor(
                doctor_id,
                request.data
            )
        )

        serializer = DoctorSerializer(
            doctor
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.DOCTOR_UPDATED,
            status_code=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        operation_description="API to delete doctor",
        request_body=DeleteDoctorApiSerializer
    )
    @action(detail=False, methods=['delete'])
    def delete_doctor(self, request):
        """
        API endpoint to delete doctor.

        This method deletes a specific doctor from the system based on the provided doctor ID.
        It uses the DoctorServiceImpl to perform the delete operation in the database and
        returns a success message indicating that the doctor was deleted successfully.

        """

        doctor_id = request.data.get(
            "doctor_id"
        )

        self.doctor_service.delete_doctor(
            doctor_id
        )

        return CustomResponse(
            data=None,
            message=SuccessMessages.DOCTOR_DELETED,
            status_code=status.HTTP_200_OK
        )