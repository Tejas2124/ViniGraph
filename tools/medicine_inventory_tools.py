from langchain.tools import tool
from databasemanagers.connection import get_db_path
import sqlite3





@tool
def list_all_medicine():
    """Lists all the medicines available in the database"""
    try:
        medicine_db = get_db_path('medicine')
        conn = sqlite3.connect(medicine_db)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT medicine from Stock;
        """)
        print('inside the list all medicine')
        medicines = cursor.fetchall()

        return [medicine[0] for medicine in medicines]
    except Exception as e:
        return f'some exception occurred: {e}'
    finally:
        if conn:
            conn.close()


@tool
def get_medicine(medicine: str, val: int):
    """Gives  medicines to  patients and updates the stock"""
    try:
        medicine_db = get_db_path('medicine')
        conn = sqlite3.connect(medicine_db)
        cursor = conn.cursor()

        # Check if medicine exists and how much stock is available
        cursor.execute("SELECT stock FROM Stock WHERE medicine = ?", (medicine.upper(),))
        result = cursor.fetchone()
        if result is None:
            return f"❌ Medicine '{medicine}' not found in stock."
        available_stock = result[0]
        if available_stock < val:
            return f"⚠️ Only {available_stock} units available for '{medicine}'. Cannot dispense {val}."

        # Deduct the required amount
        new_stock = available_stock - val
        cursor.execute("UPDATE Stock SET stock = ? WHERE medicine = ?", (new_stock, medicine.upper()))
        conn.commit()
        return f"✅ Dispensed {val} unit(s) of '{medicine}'. Remaining stock: {new_stock}"
    except Exception as e:
        return f"❌ Some exception occurred while giving medicines: {e}"
    finally:
        if conn:
            conn.close()


@tool
def add_medicine(medicine: str, quantity: int):
    """Adds medicines to the Stock , restocks old and adds new medicines"""
    try:
        medicine_db = get_db_path('medicine')
        conn = sqlite3.connect(medicine_db)
        cursor = conn.cursor()

        # Check if medicine already exists
        cursor.execute("SELECT stock FROM Stock WHERE medicine = ?", (medicine.upper(),))
        result = cursor.fetchone()

        if result:
            # Medicine exists, update stock
            new_stock = result[0] + quantity
            cursor.execute("UPDATE Stock SET stock = ? WHERE medicine = ?", (new_stock, medicine.upper()))
            conn.commit()
            return f"✅ Updated '{medicine}' stock by {quantity}. New stock: {new_stock}"
        else:
            # Medicine doesn't exist, insert new record
            cursor.execute("INSERT INTO Stock (medicine, stock) VALUES (?, ?)", (medicine.upper(), quantity))
            conn.commit()
            return f"✅ Added new medicine '{medicine}' with stock {quantity}"

    except Exception as e:
        return f"❌ Some exception occurred while adding medicine: {e}"

    finally:
        if conn:
            conn.close()

