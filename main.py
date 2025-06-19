import streamlit as st
from databases.slot_db import initialize_db,generate_daily_slots

# ✅ Only run once per Streamlit session
if "db_initialized" not in st.session_state:
    initialize_db()
    st.session_state.db_initialized = True

# ✅ Only run once per Streamlit session
if "daily_slots_generated" not in st.session_state:
    generate_daily_slots()
    st.session_state.daily_slots_generated = True