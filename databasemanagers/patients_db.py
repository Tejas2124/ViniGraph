import  os,sqlite3
from databasemanagers.connection import get_db_path

def initialize_patient_db():

    db_path = get_db_path('patients')

    # Connect to the database
    patient_conn = sqlite3.connect(db_path)
    patient_cursor = patient_conn.cursor()

    patient_cursor.execute("""
           SELECT name FROM sqlite_master WHERE type='table' AND name='patients_data';
       """)
    table_exists = patient_cursor.fetchone()

    if not table_exists:
        patient_cursor.execute("""
         CREATE TABLE patients_data (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        address TEXT NOT NULL,
        email TEXT NOT NULL
            );
        """)
        print("Patients data table created")
        patient_conn.commit()
    patient_conn.close()

