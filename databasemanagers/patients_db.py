import  os,sqlite3


def initialize_patient_db():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "databases", "patients.db")

    # Ensure the 'databases' directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

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

initialize_patient_db()