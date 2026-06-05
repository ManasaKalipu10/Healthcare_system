class PatientTestData:

    create_patient_success_payload = {
        "name": "Patient Two",
        "age": 30,
        "gender": "Male",
        "blood_group": "A+",
        "email": "patient2@test.com",
        "phone_number": "8888888888"
    }

    create_patient_invalid_payload = {
        "name": "",
        "age": "",
        "gender": "",
        "blood_group": "",
        "email": "invalid-email",
        "phone_number": ""
    }

    get_patient_success_payload = {
        "patient_id": 1
    }

    get_patient_invalid_payload = {
        "patient_id": 99999
    }

    update_patient_success_payload = {
        "patient_id": 1,
        "name": "Updated Patient",
        "age": 35,
        "gender": "Female",
        "blood_group": "B+",
        "email": "updated@test.com",
        "phone_number": "7777777777"
    }

    update_patient_invalid_payload = {
        "patient_id": 99999,
        "name": ""
    }

    delete_patient_success_payload = {
        "patient_id": 1
    }

    delete_patient_invalid_payload = {
        "patient_id": 99999
    }