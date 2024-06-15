# Orders
from enum import Enum

from pydantic import BaseModel

from models.dtos.user_dtos import UserResponse
from models.enums import OrderStatus


class OrderBase(BaseModel):
    class Config:
        from_attributes = True


class OrderResponse(OrderBase):
    id: int
    user: UserResponse
    status: OrderStatus


class OrderDelete(OrderBase):
    id: int


class OrderUpdate(OrderBase):
    id: int
    user: UserResponse | None = None
    status: OrderStatus | None = None


class OrderCreate(OrderBase):
    user_id: int
