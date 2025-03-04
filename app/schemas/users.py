from pydantic import BaseModel
from typing import Optional


class Users(BaseModel):
    userId: Optional[int] = None
    userName: Optional[str] = None
    userEmail: str
    userGender: Optional[str] = None
    userPassword: str