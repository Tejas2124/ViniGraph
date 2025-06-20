
from langchain.tools import tool
from datetime import datetime
from typing import List
import sqlite3
import os


def get_db_path(db_name:str)->str:
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, "databases", f"{db_name}.db")
        # Ensure the 'databases' directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        return db_path
    except Exception as e:
        return f'some execption {e} occured'