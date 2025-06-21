from langchain_core.tools import  tool
from typing import  Dict,Union






REQUIRED_FIELDS = ["name", "age", "gender", "phone_number", "address", "email"]

@tool
def verify_patient_data(data: Dict[str, Union[str, int]]) -> str:
    """
    Verifies that all required patient fields are present and non-empty.
    Args:
        data (dict): Patient data with fields like name, age, etc.
    Returns:
        str: Success message or list of missing/invalid fields.
    """
    missing_fields = []

    for field in REQUIRED_FIELDS:
        value = data.get(field)

        if value is None:
            missing_fields.append(field)
        elif isinstance(value, str) and not value.strip():
            missing_fields.append(field)
        elif isinstance(value, int) and field == "age" and value <= 0:
            missing_fields.append(field)  # Optional: check for valid age

    if not missing_fields:
        return "Success: All required fields are present and valid."
    else:
        return f"Missing or invalid fields: {', '.join(missing_fields)}"
