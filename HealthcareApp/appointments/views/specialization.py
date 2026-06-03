import logging
import inspect

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from WiseFlow.common.custom_response import CustomResponse
from appointments.constants.success_messages import SuccessMessages

from appointments.serializers import (
    SpecializationSerializer,
    CreateSpecializationApiSerializer,
    UpdateSpecializationApiSerializer,
    GetSpecializationDetailsApiSerializer,
    DeleteSpecializationApiSerializer
)

from appointments.services.impl.specializations_service_impl import (
    SpecializationServiceImpl
)

logger = logging.getLogger(__name__)


class SpecializationViewSet(ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.specialization_service = (
            SpecializationServiceImpl()
        )

    @swagger_auto_schema(
        operation_description="API to fetch all specializations",
        responses={
            status.HTTP_200_OK:
            SuccessMessages.SPECIALIZATIONS_FETCHED
        }
    )
    @action(detail=False, methods=['get'])
    def get_all_specializations(self, request):
        """
        API endpoint to fetch all specializations.

        This method retrieves all the specializations available in the system. 
        It uses the SpecializationsServiceImpl to fetch the data from the database and 
        returns it in a structured format using the SpecializationSerializer.
        The response includes a success message indicating that the specializations were fetched successfully.

        """

        logger.info(
            f"Entering {self.__class__.__name__}"
            f"::{inspect.currentframe().f_code.co_name}"
        )

        specializations = (
            self.specialization_service
            .get_all_specializations()
        )

        serializer = SpecializationSerializer(
            specializations,
            many=True
        )

        return CustomResponse(
            result=serializer.data,
            message=(
                SuccessMessages
                .SPECIALIZATIONS_FETCHED
            )
        )

    @swagger_auto_schema(
        operation_description="API to fetch specialization details",
        request_body=
        GetSpecializationDetailsApiSerializer
    )
    @action(detail=False, methods=['post'])
    def get_specialization_details(
        self,
        request
    ):
        """

        API endpoint to fetch specialization details.

        This method retrieves the details of a specific specialization based on the provided specialization ID.
        It uses the SpecializationsServiceImpl to fetch the data from the database and returns it in a structured format using the SpecializationSerializer.
        The response includes a success message indicating that the specialization details were fetched successfully.   

        """

        specialization_id = (
            request.data.get(
                "specialization_id"
            )
        )

        specialization = (
            self.specialization_service
            .get_specialization_details(
                specialization_id
            )
        )

        serializer = (
            SpecializationSerializer(
                specialization
            )
        )

        return CustomResponse(
            result=serializer.data,
            message=(
                SuccessMessages
                .SPECIALIZATION_FETCHED
            )
        )

    @swagger_auto_schema(
        operation_description="API to create specialization",
        request_body=
        CreateSpecializationApiSerializer
    )
    @action(detail=False, methods=['post'])
    def create_specialization(
        self,
        request
    ):
        """

        API endpoint to create specialization.

        This method handles the creation of a new specialization in the system. 
        It accepts the specialization data in the request body, validates it using the CreateSpecializationApiSerializer, 
        and then uses the SpecializationsServiceImpl to create the specialization in the database. 
        The created specialization is then serialized using the SpecializationSerializer and 
        returned in the response along with a success message indicating that the specialization was created successfully.

        """

        specialization = (
            self.specialization_service
            .create_specialization(
                request.data
            )
        )

        serializer = (
            SpecializationSerializer(
                specialization
            )
        )

        return CustomResponse(
            result=serializer.data,
            message=(
                SuccessMessages
                .SPECIALIZATION_CREATED
            )
        )

    @swagger_auto_schema(
        operation_description="API to update specialization",
        request_body=
        UpdateSpecializationApiSerializer
    )
    @action(detail=False, methods=['put'])
    def update_specialization(
        self,
        request
    ):
        """
        API endpoint to update specialization.

        This method handles the updating of an existing specialization in the system.
        It accepts the specialization ID and the updated data in the request body, validates it using the UpdateSpecializationApiSerializer,
        and then uses the SpecializationsServiceImpl to update the specialization in the database.
        The updated specialization is then serialized using the SpecializationSerializer and 
        returned in the response along with a success message indicating that the specialization was updated successfully.

        """

        specialization_id = (
            request.data.get(
                "specialization_id"
            )
        )

        specialization = (
            self.specialization_service
            .update_specialization(
                specialization_id,
                request.data
            )
        )

        serializer = (
            SpecializationSerializer(
                specialization
            )
        )

        return CustomResponse(
            result=serializer.data,
            message=(
                SuccessMessages
                .SPECIALIZATION_UPDATED
            )
        )

    @swagger_auto_schema(
        operation_description="API to delete specialization",
        request_body=
        DeleteSpecializationApiSerializer
    )
    @action(detail=False, methods=['delete'])
    def delete_specialization(
        self,
        request
    ):
        """
        API endpoint to delete specialization.

        This method handles the deletion of a specialization from the system.
        It accepts the specialization ID in the request body, validates it using the DeleteSpecializationApi
        Serializer, and then uses the SpecializationsServiceImpl to delete the specialization from the database.
        The response includes a success message indicating that the specialization was deleted successfully.
        
        """

        specialization_id = (
            request.data.get(
                "specialization_id"
            )
        )

        self.specialization_service.delete_specialization(
            specialization_id
        )

        return CustomResponse(
            result=None,
            message=(
                SuccessMessages
                .SPECIALIZATION_DELETED
            )
        )