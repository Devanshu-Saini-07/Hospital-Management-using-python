-- Create the database
CREATE DATABASE hospital_db;

-- Switch to the database
USE hospital_db;

-- Table: Patients
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender ENUM('Male','Female','Other'),
    contact VARCHAR(15),
    address VARCHAR(255)
);

-- Table: Doctors
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    contact VARCHAR(15)
);

-- Table: Appointments
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    notes VARCHAR(255),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Table: Treatments
CREATE TABLE Treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    treatment_date DATE,
    description VARCHAR(255),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Table: Billing
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    amount DECIMAL(10,2),
    bill_date DATE,
    status ENUM('Paid','Pending'),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Insert sample data
INSERT INTO Patients (name, age, gender, contact, address)
VALUES ('Riya Sharma', 29, 'Female', '9876543210', 'Jaipur');

INSERT INTO Doctors (name, specialization, contact)
VALUES ('Dr. Arjun Mehta', 'Cardiology', '9123456780');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date, notes)
VALUES (1, 1, '2026-03-30', 'Routine check-up');

INSERT INTO Treatments (patient_id, doctor_id, treatment_date, description)
VALUES (1, 1, '2026-03-30', 'ECG and blood test');

INSERT INTO Billing (patient_id, amount, bill_date, status)
VALUES (1, 1500.00, '2026-03-30', 'Pending');