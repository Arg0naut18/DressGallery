from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: Optional[str] = None
    username: str
    password: str
    email: str
    phone_number: Optional[str] = None


class UserData(BaseModel):
    username: str
    password: Optional[str] = None
    email: Optional[str] = None
