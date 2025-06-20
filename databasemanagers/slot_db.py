# slot_db.py

import sqlite3
import os
from datetime import datetime, timedelta

# Set DB path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "databases", "slot_status.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connection & Cursor (global for reuse)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def initialize_slot_db():
    global cursor
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='slots';
    """)
    if not cursor.fetchone():
        cursor.execute('''
            CREATE TABLE slots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slot TEXT NOT NULL,
                status INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        print("Db initialized-slot")
        conn.commit()

def create_slot(slot, status, date):
    cursor.execute('INSERT INTO slots (slot, status, date) VALUES (?, ?, ?)', (slot, status, date))
    conn.commit()
    print(f"✅ Slot '{slot}' created for {date} with status {status}")

def generate_daily_slots():
    today = datetime.today().date().isoformat()
    cursor.execute('SELECT COUNT(*) FROM slots WHERE date = ?', (today,))
    if cursor.fetchone()[0] > 0:
        print(f"🟢 Slots for {today} already exist.")
        return

    print(f"🛠️ Generating slots for {today}...")
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")
    duration = timedelta(minutes=20)

    while start_time < end_time:
        slot_label = f"{start_time.strftime('%I:%M %p')} - {(start_time + duration).strftime('%I:%M %p')}"
        create_slot(slot_label, 0, today)
        start_time += duration

    print("✅ Daily slot generation complete.")

def close_connection():
    conn.close()
    print("🔒 DB connection closed.")

# ✅ Wrapper to run everything ONCE at startup
def run_startup_tasks():
    initialize_slot_db()
    generate_daily_slots()
    close_connection()
