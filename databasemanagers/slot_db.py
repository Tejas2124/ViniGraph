import sqlite3
from datetime import datetime, timedelta

# Connect to SQLite database
slot_conn = sqlite3.connect("slot_status.db")
slot_cursor = slot_conn.cursor()



def initialize_slot_db():
    conn = sqlite3.connect("slot_status.db")
    cursor = conn.cursor()

    # Check if table exists
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='slots';
    """)
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute('''
            CREATE TABLE slots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slot TEXT NOT NULL,
                status INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
    conn.close()







def create_slot(slot, status, date):
    slot_cursor.execute('INSERT INTO slots (slot, status, date) VALUES (?, ?, ?)', (slot, status, date))
    slot_conn.commit()
    print(f"✅ Slot '{slot}' created for {date} with status {status}")


def generate_daily_slots():
    today = datetime.today().date().isoformat()

    # Check if today's slots are already created
    slot_cursor.execute('SELECT COUNT(*) FROM slots WHERE date = ?', (today,))
    if slot_cursor.fetchone()[0] > 0:
        print(f"🟢 Slots for {today} already exist.")
        return

    # Generate 20-minute slots from 9:00 AM to 5:00 PM
    print(f"🛠️ Generating slots for {today}...")
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")
    duration = timedelta(minutes=20)

    while start_time < end_time:
        slot_label = f"{start_time.strftime('%I:%M %p')} - {(start_time + duration).strftime('%I:%M %p')}"
        create_slot(slot_label, 0, today)
        start_time += duration

    print("✅ Daily slot generation complete.")