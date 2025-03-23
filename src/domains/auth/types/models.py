from datetime import datetime
from pydantic import BaseModel, EmailStr


class AuthUser(BaseModel):
    email: EmailStr
    password: str


class RefreshToken(BaseModel):
    refresh_token: str


class UserInfo(BaseModel):
    email: str
    name: str
    user_type: str
    created_at: datetime


class Token(BaseModel):
    access_token: str
    refresh_token: str
