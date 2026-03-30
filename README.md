# Hospital Management using C
🏥 Hospital Management System
A simple Hospital Management System built with Python and MySQL.
This project demonstrates how to manage patients, doctors, appointments, treatments, billing, and medicines with a menu-driven console application. It also supports CSV import/export for easy data backup and restore.

📂 Features
- Patients
- Add / View patient details
- Export / Import patient records to/from CSV
- Doctors
- Add / View doctor details
- Export / Import doctor records to/from CSV
- Appointments
- Schedule / View appointments
- Export / Import appointment records to/from CSV
- Treatments
- Record / View treatments
- Export / Import treatment records to/from CSV
- Billing
- Add / View bills
- Export / Import billing records to/from CSV
- Medicines
- Record medicines prescribed to patients
- View medicines by patient

🗄️ Database Schema
The system uses a MySQL database named hospital_db with the following tables:
- Patients: patient details
- Doctors: doctor details
- Appointments: links patients and doctors with appointment date/notes
- Treatments: records treatments given by doctors to patients
- Billing: tracks bills and payment status
- Patient_Medicines: medicines prescribed to patients

🐍 Python Program
- Menu-driven console interface
- Each section (Patients, Doctors, Appointments, Treatments, Billing) has:
- Add / View options
- CSV export/import integrated into the View option
- Uses mysql.connector for database connection
- Uses Python’s built-in csv module for CSV handling

▶️ How to Run
- Install MySQL and create the database:
CREATE DATABASE hospital_db;
- Then run the schema SQL file to create tables.
- Install required Python package:
pip install mysql-connector-python
- Update database credentials in connect_db():
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="hospital_db"
    )
- Run the program:
python hospital.py
📤 CSV Export/Import- When you view records, the program asks:
Do you want to export these records to CSV? (y/n)
- If you choose y, a CSV file is created (e.g., patients.csv).
- You can also import records back from CSV files.
📌 Future Improvements- Add update/delete options for full CRUD functionality
- Build a web interface using Flask/Django
- Add report generation (e.g., pending bills, today’s appointments)
🤝 ContributingFeel free to fork this repository, suggest improvements, or add new features like:- Role-based access (Admin/Doctor/Receptionist)
- Advanced reporting
- Integration with external APIs