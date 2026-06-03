import logging

from appointments.dao.impl.patient_dao_impl import (
    PatientDAOImpl
)


from appointments.services.interface.patient_service_interface import (
    PatientServiceInterface
)

logger = logging.getLogger(__name__)

class PatientServiceImpl(
    PatientServiceInterface
):

    def __init__(self):

        self.patient_dao = PatientDAOImpl()

    def get_all_patients(self):

        logger.info(
            "Patient service: fetching all patients"
        )

        return self.patient_dao.get_all_patients()

    def create_patient(
        self,
        patient_data
    ):

        logger.info(
            "Patient service: creating patient"
        )

        return self.patient_dao.create_patient(
            patient_data
        )

    def get_patient_details(
        self,
        patient_id
    ):

        logger.info(
            f"Patient service: fetching patient {patient_id}"
        )

        return self.patient_dao.get_patient_details(
            patient_id
        )

    def update_patient(
        self,
        patient_id,
        patient_data
    ):

        logger.info(
            f"Patient service: updating patient {patient_id}"
        )

        return self.patient_dao.update_patient(
            patient_id,
            patient_data
        )

    def delete_patient(self, patient_id):

        logger.info(
            f"Patient service: deleting patient {patient_id}"
        )

        return self.patient_dao.delete_patient(
            patient_id
        )