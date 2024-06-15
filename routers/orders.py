from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.dtos import OrderResponse, OrderCreate, OrderUpdate, OrderDelete, OrderStatus
from models.models import Order

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.get("/")
def read_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@router.get("/{username}", response_model=OrderResponse)
def read_order_by_username(username: str, db: Session = Depends(get_db)):
    db_item: Order = db.query(Order).filter(Order.user.username == username).first()
    if db_item is None:
        return HTTPException(404)
    return db_item


@router.post("/", response_model=OrderResponse)
def create_order(user: OrderCreate, db: Session = Depends(get_db)):
    db_item: Order = Order(**user.model_dump())
    db_item.status = OrderStatus.ORDER_INIT
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.patch("/", response_model=OrderResponse)
def update_order(order: OrderUpdate, db: Session = Depends(get_db)):
    db_item: Order | None = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        return HTTPException(404)
    db_item.status = order.user if order.user is not None else db_item.user
    db_item.status = order.status if order.status is not None else db_item.status
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/", response_model=OrderResponse)
async def cancel_order(order: OrderDelete, db: Session = Depends(get_db)) -> None:
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        return HTTPException(404)
    db_item.status = OrderStatus.ORDER_CANCELED
    db.commit()
    db.refresh(db_item)
    return


@router.delete("/", response_model=OrderResponse)
async def delete_order(order: OrderDelete, db: Session = Depends(get_db)) -> None:
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        return HTTPException(404)
    db.delete(db_item)
    db.commit()
    return
