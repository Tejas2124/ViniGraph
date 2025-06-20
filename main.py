import streamlit as st
from databasemanagers.slot_db import run_startup_tasks
from databasemanagers.medicine_db import initialize_medicine_db,generate_basic_stock
from tools.medicine_inventory_tools import list_all_medicine
from tools.scheduler_tools import view_available_slots

# ✅ Only run once per Streamlit session
if "run_startup_tasks" not in st.session_state:
    run_startup_tasks()
    st.session_state.run_startup_tasks = True


lst = list_all_medicine.invoke({})

