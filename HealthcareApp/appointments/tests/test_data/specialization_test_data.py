class SpecializationTestData:

    create_specialization_success_payload = {
        "name": "Neurology"
    }

    create_specialization_invalid_payload = {
        "name": ""
    }

    get_specialization_success_payload = {
        "specialization_id": 1
    }

    get_specialization_invalid_payload = {
        "specialization_id": 99999
    }

    update_specialization_success_payload = {
        "specialization_id": 1,
        "name": "Updated Neurology"
    }

    update_specialization_invalid_payload = {
        "specialization_id": 99999,
        "name": "Updated Neurology"
    }

    delete_specialization_success_payload = {
        "specialization_id": 1
    }

    delete_specialization_invalid_payload = {
        "specialization_id": 99999
    }