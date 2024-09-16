
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_info: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    birthday: Optional[date]
    additional_info: Optional[str] = None

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
