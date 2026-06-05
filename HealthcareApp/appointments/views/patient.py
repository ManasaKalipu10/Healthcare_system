import logging
import inspect

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from WiseFlow.common.custom_response import CustomResponse
from appointments.constants.success_messages import SuccessMessages

from appointments.serializers import (
    PatientSerializer,
    CreatePatientApiSerializer,
    UpdatePatientApiSerializer,
    GetPatientDetailsApiSerializer,
    DeletePatientApiSerializer
)

from appointments.services.impl.patient_service_impl import (
    PatientServiceImpl
)

logger = logging.getLogger(__name__)


class PatientViewSet(ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.patient_service = (
            PatientServiceImpl()
        )
    @swagger_auto_schema(
        operation_description="API to fetch all patients",
        responses={
            status.HTTP_200_OK: SuccessMessages.PATIENTS_FETCHED
        }
    )
    @action(detail=False, methods=['get'])
    def get_all_patients(self, request):
        """
        API endpoint to fetch all patients.

        This method retrieves all the patients available in the system. 
        It uses the PatientServiceImpl to fetch the data from the database and 
        returns it in a structured format using the PatientSerializer.
        The response includes a success message indicating that the patients were fetched successfully.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        patients = (
            self.patient_service
            .get_all_patients()
        )

        serializer = PatientSerializer(
            patients,
            many=True
        )

        return CustomResponse(  
            data=serializer.data,
            message=SuccessMessages.PATIENTS_FETCHED,
            status_code=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(
        operation_description="API to fetch patient details",
        request_body=GetPatientDetailsApiSerializer
    )
    @action(detail=False, methods=['post'])
    def get_patient_details(self, request): 
        """
        API endpoint to fetch patient details.

        This method retrieves the details of a specific patient based on the provided patient ID. 
        It uses the PatientServiceImpl to fetch the data from the database and 
        returns it in a structured format using the PatientSerializer.
        The response includes a success message indicating that the patient details were fetched successfully.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        patient_id = request.data.get("patient_id")

        patient = (
            self.patient_service
            .get_patient_details(patient_id)
        )

        serializer = PatientSerializer(
            patient
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.PATIENT_DETAILS_FETCHED,
            status_code=status.HTTP_200_OK
        )   
    
    @swagger_auto_schema(
        operation_description="API to create patient",
        request_body=CreatePatientApiSerializer
    )
    @action(detail=False, methods=['post'])
    def create_patient(self, request):
        """
        API endpoint to create patient.

        This method creates a new patient in the system based on the provided data.
        It uses the PatientServiceImpl to save the data to the database and 
        returns the created patient details in a structured format using the PatientSerializer.
        The response includes a success message indicating that the patient was created successfully.

        """

        patient = (
            self.patient_service
            .create_patient(request.data)
        )

        serializer = PatientSerializer(
            patient
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.PATIENT_CREATED,
            status_code=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(
        operation_description="API to update patient details",
        request_body=UpdatePatientApiSerializer
    )
    @action(detail=False, methods=['put'])
    def update_patient(self, request):
        """
        API endpoint to update patient details.

        This method updates the details of an existing patient in the system based on the provided data.
        It uses the PatientServiceImpl to update the data in the database and 
        returns the updated patient details in a structured format using the PatientSerializer.
        The response includes a success message indicating that the patient details were updated successfully.

        """

        patient_id = request.data.get("patient_id")

        patient = (
            self.patient_service
            .update_patient(patient_id, request.data)
        )

        serializer = PatientSerializer(
            patient
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.PATIENT_UPDATED,
            status_code=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(
        operation_description="API to delete patient",
        request_body=DeletePatientApiSerializer
    )
    @action(detail=False, methods=['delete'])
    def delete_patient(self, request):  
        """
        API endpoint to delete patient.

        This method deletes an existing patient from the system based on the provided patient ID.
        It uses the PatientServiceImpl to delete the data from the database and 
        returns a success message indicating that the patient was deleted successfully.

        """

        patient_id = request.data.get("patient_id")
        patient = (
            self.patient_service
            .delete_patient(patient_id, request.data)
        )

        self.patient_service.delete_patient(patient_id)
        serializer = PatientSerializer(
            patient
        )

        return CustomResponse(
            data=serializer.data,
            message=SuccessMessages.PATIENT_DELETED,
            status_code=status.HTTP_200_OK
        )