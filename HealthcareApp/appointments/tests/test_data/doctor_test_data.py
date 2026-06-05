class DoctorTestData:

    create_doctor_success_payload = {
        "name": "Doctor Two",
        "email": "doctor2@test.com",
        "phone_number": "9876543210",
        "years_of_experience": 10,
        "specialization": 1
    }

    create_doctor_invalid_payload = {
        "name": "",
        "email": "",
        "phone_number": "",
        "years_of_experience": "",
        "specialization": ""
    }

    get_doctor_success_payload = {
        "doctor_id": 1
    }

    get_doctor_invalid_payload = {
        "doctor_id": ""
    }

    update_doctor_success_payload = {
        "doctor_id": 1,
        "name": "Updated Doctor"
    }

    update_doctor_invalid_payload = {
        "doctor_id": "",
        "name": ""
    }

    delete_doctor_success_payload = {
        "doctor_id": 1
    }

    delete_doctor_invalid_payload = {
        "doctor_id": ""
    }