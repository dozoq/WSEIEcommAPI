from enum import Enum

from pydantic import BaseModel

from models.models import User


# Articles
class ArticleGet(BaseModel):
    name: str
    description: str


class ArticleCreate(BaseModel):
    name: str
    description: str


class ArticleUpdate(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None


class ArticleDelete(BaseModel):
    id: int


class ArticleResponse(BaseModel):
    id: int
    name: str
    description: str


# Users
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


class UserUpdate(BaseModel):
    id: int
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    password: str | None = None


class UserDelete(BaseModel):
    id: int


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str


# Orders
class OrderStatus(str, Enum):
    ORDER_INIT = "Order Initialized"
    ORDER_PAID = "Order Paid"
    ORDER_ARTICLES_CONFIRMED = "Order articles confirmed"
    ORDER_ARTICLES_DENIED = "Order articles denied"
    ORDER_BEING_PACKED = "Order being packed"
    ORDER_SENT = "Order sent"
    ORDER_DELIVERED = "Order delivered"
    ORDER_CANCELED = "Order canceled"


class OrderResponse:
    id: int
    user: User
    status: OrderStatus


class OrderDelete:
    id: int


class OrderUpdate:
    id: int
    user: User | None = None
    status: OrderStatus | None = None


class OrderCreate:
    id: int
    user: User
