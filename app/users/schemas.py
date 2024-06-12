from pydantic import BaseModel, EmailStr

class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserRegister(BaseModel):
    email: EmailStr
    password: str
    

