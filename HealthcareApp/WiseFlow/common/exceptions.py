from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status

from WiseFlow.common.custom_response import (
    CustomResponse
)

from appointments.constants.error_messages import (
    ErrorMessages
)


class CustomAPIException(APIException):

    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(
        self,
        detail=None,
        status_code=None
    ):

        self.status_code = (
            status_code
            if status_code
            else self.status_code
        )

        self.detail = (
            detail
            if detail
            else ErrorMessages.VALIDATION_ERROR
        )


class ValidationError(
    CustomAPIException
):
    """
    Validation Exception
    """

    status_code = (
        status.HTTP_400_BAD_REQUEST
    )


class ResourceNotFoundError(
    CustomAPIException
):
    """
    Resource Not Found Exception
    """

    status_code = (
        status.HTTP_404_NOT_FOUND
    )


class DoctorNotFoundError(
    ResourceNotFoundError
):

    def __init__(self, doctor_id):

        super().__init__(
            detail=f"Doctor with ID {doctor_id} not found.",
            status_code=status.HTTP_404_NOT_FOUND
        )


class PatientNotFoundError(
    ResourceNotFoundError
):

    def __init__(self, patient_id):

        super().__init__(
            detail=f"Patient with ID {patient_id} not found.",
            status_code=status.HTTP_404_NOT_FOUND
        )


class AppointmentNotFoundError(
    ResourceNotFoundError
):

    def __init__(self, appointment_id):

        super().__init__(
            detail=f"Appointment with ID {appointment_id} not found.",
            status_code=status.HTTP_404_NOT_FOUND
        )

class SpecializationNotFoundError(
    ResourceNotFoundError
):

    def __init__(self, speciality_id):

        super().__init__(
            detail=f"Specialization with ID {speciality_id} not found.",
            status_code=status.HTTP_404_NOT_FOUND
        )

def custom_exception_handler(
    exc,
    context
):

    response = exception_handler(
        exc,
        context
    )

    if response is not None:

        return CustomResponse(
            data=None,
            message="Validation error",
            success=False,
            status_code=response.status_code
        )

    return CustomResponse(
        data=None,
        message=ErrorMessages.INTERNAL_SERVER_ERROR,
        success=False,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )