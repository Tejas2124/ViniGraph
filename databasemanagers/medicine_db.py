import os
import sqlite3
from databasemanagers.connection import get_db_path
from prompts.medicine_inventory_prompt import medicine_inventory_system_prompt

path = get_db_path('medicine')
medicine_conn = sqlite3.connect(path)
medicine_cursor = medicine_conn.cursor()

def initialize_medicine_db():


    medicine_cursor.execute("""
     SELECT name FROM sqlite_master WHERE type='table' AND name='Stock';
     """)

    table_exists = medicine_cursor.fetchone()

    if not table_exists:

        medicine_cursor.execute('''
                    CREATE TABLE Stock (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        medicine TEXT NOT NULL,
                        stock INTEGER NOT NULL
                    )
                ''')
        generate_basic_stock()
        print("medicine-db initialization process completed")
        medicine_conn.commit()

    medicine_conn.close()

def generate_basic_stock():

    global medicine_conn,medicine_cursor

    medicine_cursor.execute("insert into Stock (id,medicine,stock) VALUES (1,'PARACETAMOL',20),(2,'CETRIZINE',20),(3,'COMBIFLAM',20),(4,'SACNOVA',20),(5,'PDAP',20),(6,'DICLOFANAC',20);")
    print("Basic Stock Generated ")






