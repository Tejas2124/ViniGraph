from langchain_core.tools import  tool
from typing import  Dict,Union,List
import sqlite3


@tool
def insert_patient_from_dict(patient_data: Dict) -> str:
    """
    Inserts a new patient into the patients_data SQLite table using dictionary input.
    Args:
        patient_data (dict): A dictionary with keys: name, age, gender, phone_number, address, email
    Returns:
        str: Success message or error detail
    """
    required_fields = ["name", "age", "gender", "phone_number", "address", "email"]

    # Check if all required keys are present
    for field in required_fields:
        if field not in patient_data:
            return f"Missing required field: {field}"

    try:
        conn = sqlite3.connect("patients.db")
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO patients_data (name, age, gender, phone_number, address, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(insert_query, (
            patient_data["name"],
            int(patient_data["age"]),
            patient_data["gender"],
            patient_data["phone_number"],
            patient_data["address"],
            patient_data["email"]
        ))

        conn.commit()
        inserted_id = cursor.lastrowid
        return f"Patient inserted successfully with ID: {inserted_id}"

    except sqlite3.Error as e:
        return f"Error inserting patient: {e}"

    finally:
        conn.close()


@tool
def get_patient_details(identifier: Union[int, str]) -> Union[str, List[dict]]:
    """
    Fetches patient details using patient ID or (partial) name.

    Args:
        identifier (int | str): Patient ID (int) or name (str) or partial name

    Returns:
        list of dict: List of matching patient records
        str: Message if no patients found or error occurred
    """

    try:
        conn = sqlite3.connect("patients.db")
        cursor = conn.cursor()

        # Search by ID
        if isinstance(identifier, int):
            query = "SELECT * FROM patients_data WHERE patient_id = ?"
            cursor.execute(query, (identifier,))
            rows = cursor.fetchall()

        # Search by name (partial or full)
        else:
            query = "SELECT * FROM patients_data WHERE name LIKE ?"
            search_term = f"%{identifier.strip()}%"  # partial name match
            cursor.execute(query, (search_term,))
            rows = cursor.fetchall()

        if not rows:
            msg = f"No patient found with {'ID' if isinstance(identifier, int) else 'name'}: {identifier}"
            return msg

        # Format the results
        patients = []
        for row in rows:
            patients.append({
                "patient_id": row[0],
                "name": row[1],
                "age": row[2],
                "gender": row[3],
                "phone_number": row[4],
                "address": row[5],
                "email": row[6]
            })

        return patients

    except sqlite3.Error as e:
        error_msg = f"Database error: {e}"
        return error_msg

    finally:
        conn.close()