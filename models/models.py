from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship

from models.db import Base
from models.enums import OrderStatus


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)


class Order(Base):
    __tablename__ = "order"
    id: int = Column(Integer, primary_key=True, index=True)
    status: OrderStatus = Column(SQLAlchemyEnum(OrderStatus), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="orders")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String, index=True)
    username = Column(String, index=True)
    password = Column(String)
    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user")


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="cart")

