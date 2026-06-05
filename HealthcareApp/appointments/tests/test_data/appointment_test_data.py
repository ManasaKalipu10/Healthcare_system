class AppointmentTestData:

    # ---------------- CREATE ----------------

    create_appointment_success_payload = {
        "doctor": 1,
        "patient": 1,
        "appointment_date": "2026-06-10",
        "appointment_time": "10:00:00",
        "symptoms": "Fever"
    }

    create_appointment_invalid_payload = {
        "doctor": "",
        "patient": "",
        "appointment_date": "",
        "appointment_time": "",
        "symptoms": ""
    }

    create_appointment_invalid_response = {
        "success": False,
        "message": "Validation error",
        "data": None
    }

    # ---------------- GET DETAILS ----------------

    get_appointment_success_payload = {
        "appointment_id": 1
    }

    get_appointment_invalid_payload = {
        "appointment_id": ""
    }

    get_appointment_not_found_response = {
        "success": False,
        "message": "Appointment with ID 9999 not found.",
        "data": None
    }

    # ---------------- UPDATE ----------------

    update_appointment_success_payload = {
        "appointment_id": 1,
        "symptoms": "Severe fever"
    }

    update_appointment_invalid_payload = {
        "appointment_id": "",
        "symptoms": ""
    }

    update_appointment_not_found_response = {
        "success": False,
        "message": "Appointment with ID 9999 not found.",
        "data": None
    }

    # ---------------- CANCEL ----------------

    cancel_appointment_success_payload = {
        "appointment_id": 1
    }

    cancel_appointment_invalid_payload = {
        "appointment_id": ""
    }

    cancel_appointment_not_found_response = {
        "success": False,
        "message": "Appointment with ID 9999 not found.",
        "data": None
    }

    # ---------------- SLOT CHECK ----------------

    check_slot_success_payload = {
        "doctor_id": 1,
        "appointment_date": "2026-06-10",
        "appointment_time": "10:00:00"
    }

    check_slot_invalid_payload = {
        "doctor_id": "",
        "appointment_date": "",
        "appointment_time": ""
    }