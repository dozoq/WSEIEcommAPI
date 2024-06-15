from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum

from models.db import Base
from models.enums import OrderStatus


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String, index=True)
    username = Column(String, index=True)
    password = Column(String)


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    user = ForeignKey("user.id")


class Order(Base):
    __tablename__ = "order"
    id: int = Column(Integer, primary_key=True, index=True)
    user: User = ForeignKey("user.id", index=True)
    status: OrderStatus = Column(SQLAlchemyEnum(OrderStatus), nullable=False)
