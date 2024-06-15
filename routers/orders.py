from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from models.db import get_db
from models.dtos.order_dtos import OrderResponse, OrderCreate, OrderUpdate, OrderDelete, OrderStatus
from models.dtos.user_dtos import UserResponse
from models.models import Order, User

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.get("/")
def read_orders(db: Session = Depends(get_db)) -> List[OrderResponse]:
    list_of_orders_to_convert = db.query(Order).options(joinedload(Order.user)).all()
    converted_list = [
        OrderResponse(
            id=order.id,
            user=UserResponse.from_orm(order.user),
            status=order.status
        )
        for order in list_of_orders_to_convert
    ]
    return list_of_orders_to_convert


@router.get("/{username}", response_model=OrderResponse)
def read_order_by_username(username: str, db: Session = Depends(get_db)) -> OrderResponse:
    db_item: Order = db.query(Order).filter(Order.user.username == username).first()
    if db_item is None:
        return HTTPException(404)
    return OrderResponse.from_orm(db_item)


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)) -> OrderResponse:
    db_user = db.query(User).filter(User.id == order.user_id).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    db_item = Order(user_id=order.user_id, status=OrderStatus.ORDER_INIT)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.patch("/", response_model=OrderResponse)
def update_order(order: OrderUpdate, db: Session = Depends(get_db)) -> OrderResponse:
    db_item: Order | None = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        return HTTPException(404)
    db_item.status = order.user if order.user is not None else db_item.user
    db_item.status = order.status if order.status is not None else db_item.status
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/cancel", response_model=OrderResponse)
async def cancel_order(order: OrderDelete, db: Session = Depends(get_db)) -> OrderResponse:
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        return HTTPException(404)
    db_item.status = OrderStatus.ORDER_CANCELED
    db.commit()
    db.refresh(db_item)
    return


@router.delete("/", response_model=None)
async def delete_order(order: OrderDelete, db: Session = Depends(get_db)) -> None:
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        return HTTPException(404)
    db.delete(db_item)
    db.commit()
    return
