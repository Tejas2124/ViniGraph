from databasemanagers.connection import get_db_path
from langchain.tools import tool
from datetime import datetime
from typing import List
import sqlite3



db_path = get_db_path('slot_status')

# Connection & Cursor (global for reuse)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()



@tool
def book_slot(slot_id: int):
    """Books available slot on today using slot_id"""
    # These should be already defined in your file:
    global conn,cursor
    slot_conn = conn
    slot_cursor = cursor
    today = datetime.today().date().isoformat()
    slot_cursor.execute('SELECT status FROM slots WHERE id = ? AND date = ?', (slot_id, today))
    row = slot_cursor.fetchone()
    if row is None:
        return f"❌ Slot ID {slot_id} is invalid for today."
    elif row[0] == 1:
        return f"⚠️ Slot ID {slot_id} is already booked."
    else:
        slot_cursor.execute('UPDATE slots SET status = 1 WHERE id = ? AND date = ?', (slot_id, today))
        slot_conn.commit()
        return f"✅ Slot ID {slot_id} booked successfully."

@tool
def view_available_slots() -> List:
    """Lists today's available slots"""
    # These should be already defined in your file:
    global conn,cursor
    slot_conn = conn
    slot_cursor = cursor
    today = datetime.today().date().isoformat()
    slot_cursor.execute('SELECT id, slot FROM slots WHERE status = 0 AND date = ?', (today,))
    slots = slot_cursor.fetchall()
    if not slots:
        return ["❌ No available slots for today."]
    return [{"id": slot[0], "time": slot[1]} for slot in slots]