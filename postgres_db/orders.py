from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    customer_id: int
    status: str
    order_date: datetime
    delivery_date: Optional[datetime]
    total_amount: float



class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    order_id: int
    order_date: datetime
    total_amount: float

    class Config:
        from_attributes = True


class OrderDetailBase(BaseModel):
    product_id: int
    quantity: int
    price_per_unit: float
    total_price: float


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailRead(OrderDetailBase):
    order_detail_id: int

    class Config:
        from_attributes = True