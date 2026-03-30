import mysql.connector;
import csv;

# ---------------- Database Connection ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # replace with your MySQL user
        password="12345",  # replace with your MySQL password
        database="hospital_db"     # matches your schema
    )

# ---------------- Patients ----------------
def add_patient():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (Male/Female/Other): ")
    contact = input("Enter contact: ")
    address = input("Enter address: ")

    sql = "INSERT INTO Patients (name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (name, age, gender, contact, address))
    conn.commit()
    print("Patient added successfully!")
    conn.close()

def view_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patients")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def export_patients_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patients")
    rows = cursor.fetchall()
    with open("patients.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(rows)
    print("Patients exported to patients.csv successfully!")
    conn.close()

def import_patients_from_csv():
    conn = connect_db()
    cursor = conn.cursor()
    with open("patients.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            sql = "INSERT INTO Patients (patient_id, name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, row)
    conn.commit()
    print("Patients imported from patients.csv successfully!")
    conn.close()


# ---------------- Doctors ----------------
def add_doctor():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    contact = input("Enter contact: ")

    sql = "INSERT INTO Doctors (name, specialization, contact) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, specialization, contact))
    conn.commit()
    print("Doctor added successfully!")
    conn.close()

def view_doctors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Doctors")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def export_doctors_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Doctors")
    rows = cursor.fetchall()
    with open("doctors.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(rows)
    print("Doctors exported to doctors.csv successfully!")
    conn.close()

def import_doctors_from_csv():
    conn = connect_db()
    cursor = conn.cursor()
    with open("doctors.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sql = "INSERT INTO Doctors (doctor_id, name, specialization, contact) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, row)
    conn.commit()
    print("Doctors imported from doctors.csv successfully!")
    conn.close()

# ---------------- Appointments ----------------
def add_appointment():
    conn = connect_db()
    cursor = conn.cursor()
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    notes = input("Enter notes: ")

    sql = "INSERT INTO Appointments (patient_id, doctor_id, appointment_date, notes) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (patient_id, doctor_id, appointment_date, notes))
    conn.commit()
    print("Appointment scheduled successfully!")
    conn.close()

def view_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointments")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def export_appointments_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointments")
    rows = cursor.fetchall()
    with open("appointments.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(rows)
    print("Appointments exported to appointments.csv successfully!")
    conn.close()

def import_appointments_from_csv():
    conn = connect_db()
    cursor = conn.cursor()
    with open("appointments.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sql = "INSERT INTO Appointments (appointment_id, patient_id, doctor_id, appointment_date, notes) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, row)
    conn.commit()
    print("Appointments imported from appointments.csv successfully!")
    conn.close()

# ---------------- Treatments ----------------
def add_treatment():
    conn = connect_db()
    cursor = conn.cursor()
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    treatment_date = input("Enter treatment date (YYYY-MM-DD): ")
    description = input("Enter treatment description: ")

    sql = "INSERT INTO Treatments (patient_id, doctor_id, treatment_date, description) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (patient_id, doctor_id, treatment_date, description))
    conn.commit()
    print("Treatment record added successfully!")
    conn.close()

def view_treatments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Treatments")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def export_treatments_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Treatments")
    rows = cursor.fetchall()
    with open("treatments.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(rows)
    print("Treatments exported to treatments.csv successfully!")
    conn.close()

def import_treatments_from_csv():
    conn = connect_db()
    cursor = conn.cursor()
    with open("treatments.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sql = "INSERT INTO Treatments (treatment_id, patient_id, doctor_id, treatment_date, description) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, row)
    conn.commit()
    print("Treatments imported from treatments.csv successfully!")
    conn.close()

# ---------------- Billing ----------------
def add_bill():
    conn = connect_db()
    cursor = conn.cursor()
    patient_id = int(input("Enter patient ID: "))
    amount = float(input("Enter bill amount: "))
    bill_date = input("Enter bill date (YYYY-MM-DD): ")
    status = input("Enter status (Paid/Pending): ")

    sql = "INSERT INTO Billing (patient_id, amount, bill_date, status) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (patient_id, amount, bill_date, status))
    conn.commit()
    print("Bill added successfully!")
    conn.close()

def view_bills():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Billing")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def export_billing_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Billing")
    rows = cursor.fetchall()
    with open("billing.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(rows)
    print("Billing exported to billing.csv successfully!")
    conn.close()

def import_billing_from_csv():
    conn = connect_db()
    cursor = conn.cursor()
    with open("billing.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sql = "INSERT INTO Billing (bill_id, patient_id, amount, bill_date, status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, row)
    conn.commit()
    print("Billing imported from billing.csv successfully!")
    conn.close()

# ---------------- Menu ----------------
def main_menu():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Add Appointment")
        print("6. View Appointments")
        print("7. Add Treatment")
        print("8. View Treatments")
        print("9. Add Bill")
        print("10. View Bills")
        print("11. Export Patients to CSV")
        print("12. Import Patients from CSV")
        print("13. Export Doctors to CSV")
        print("14. Import Doctors from CSV")
        print("15. Export Appointments to CSV")
        print("16. Import Appointments from CSV")
        print("17. Export Treatments to CSV")
        print("18. Import Treatments from CSV")
        print("19. Export Billing to CSV")
        print("20. Import Billing from CSV")
        print("21. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_doctor()
        elif choice == "4":
            view_doctors()
        elif choice == "5":
            add_appointment()
        elif choice == "6":
            view_appointments()
        elif choice == "7":
            add_treatment()
        elif choice == "8":
            view_treatments()
        elif choice == "9":
            add_bill()
        elif choice == "10":
            view_bills()
        elif choice == "11":
            export_patients_to_csv()
        elif choice == "12":
            import_patients_from_csv()
        elif choice == "13":
            export_doctors_to_csv()
        elif choice == "14":
            import_doctors_from_csv()
        elif choice == "15":
            export_appointments_to_csv()
        elif choice == "16":
            import_appointments_from_csv()
        elif choice == "17":
            export_treatments_to_csv()
        elif choice == "18":
            import_treatments_from_csv()
        elif choice == "19":
            export_billing_to_csv()
        elif choice == "20":
            import_billing_from_csv()
        elif choice == "21":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()