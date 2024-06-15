# Orders
from enum import Enum

from pydantic import BaseModel

from models.models import User


class OrderStatus(str, Enum):
    ORDER_INIT = "Order Initialized"
    ORDER_PAID = "Order Paid"
    ORDER_ARTICLES_CONFIRMED = "Order articles confirmed"
    ORDER_ARTICLES_DENIED = "Order articles denied"
    ORDER_BEING_PACKED = "Order being packed"
    ORDER_SENT = "Order sent"
    ORDER_DELIVERED = "Order delivered"
    ORDER_CANCELED = "Order canceled"


class OrderResponse(BaseModel):
    id: int
    user: User
    status: OrderStatus


class OrderDelete(BaseModel):
    id: int


class OrderUpdate(BaseModel):
    id: int
    user: User | None = None
    status: OrderStatus | None = None


class OrderCreate(BaseModel):
    id: int
    user: User
