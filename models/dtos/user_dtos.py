# Users
from pydantic import BaseModel


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

