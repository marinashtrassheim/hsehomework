from pydantic import BaseModel, EmailStr, constr, field_validator
from datetime import datetime
import re


class CustomerBase(BaseModel):
    full_name: constr(max_length=50)
    email: EmailStr
    created_at: datetime




class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    user_id: int
    registration_date: datetime

    class Config:
        from_attributes = True