from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str


