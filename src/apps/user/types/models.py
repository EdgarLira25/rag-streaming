from pydantic import BaseModel, EmailStr, Field


class CreateUserPayload(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=250)
    name: str = Field(max_length=250)
