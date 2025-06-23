from pydantic import BaseModel

class Dataschema(BaseModel):
    name: str = None
    age: int = None
    sex: str = None
    phone_number: str = None
    email: str = None
    address: str = None
