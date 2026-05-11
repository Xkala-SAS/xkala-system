from pydantic import BaseModel
from datetime import datetime




class LoginRequest(BaseModel):
    numero_documento: str
    password: str