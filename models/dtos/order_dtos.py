# Orders
from enum import Enum

from pydantic import BaseModel

from models.dtos.user_dtos import UserResponse, UserUpdate
from models.enums import OrderStatus


class OrderBase(BaseModel):
    class Config:
        from_attributes = True


class OrderPointer(OrderBase):
    id: int


class OrderFullData(OrderBase):
    id: int
    user: UserResponse
    status: OrderStatus
    tracking_number: str | None = None


class OrderResponse(OrderBase):
    id: int
    user: UserResponse
    status: OrderStatus


class OrderDelete(OrderBase):
    id: int


class OrderUpdate(OrderBase):
    id: int
    user: UserUpdate | None = None
    status: OrderStatus | None = None


class OrderCreate(OrderBase):
    user_id: int
