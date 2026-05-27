CREATE TABLE appointments_specialization (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE doctor (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) ,
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(15) ,
    years_of_experience INTEGER ,
    specialization_id INTEGER 
);

CREATE TABLE patient (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) ,
    age INTEGER ,
    gender VARCHAR(10) ,
    blood_group VARCHAR(5) ,
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(15) 
);

CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    appointment_date DATE ,
    appointment_time TIME ,
    symptoms TEXT,
     doctor_id INTEGER ,
    patient_id INTEGER 
);