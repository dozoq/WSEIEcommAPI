# Users
from pydantic import BaseModel


class UserBase(BaseModel):
    class Config:
        from_attributes = True


class UserPointer(UserBase):
    id: int


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class UserUpdate(UserBase):
    id: int
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    password: str | None = None
    email: str | None = None


class UserDelete(UserBase):
    id: int


class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

