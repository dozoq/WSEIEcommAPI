from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from models.db import get_db
from models.dtos.order_dtos import OrderPointer
from models.models import Order
from services.factories.payment_service_factory import PaymentServiceFactory

router = APIRouter(
    prefix="/payment",
)


@router.get("/{order_id}", tags=["payment"], response_model=str)
def get_payment_url(order_id: str, db: Session = Depends(get_db)) -> str:
    db_item: Order = db.query(Order).filter(Order.id == order_id).first()
    if db_item is None:
        raise HTTPException(404)
    payment_provider = PaymentServiceFactory.get_provider()
    return payment_provider.get_payment_url(OrderPointer.from_orm(db_item))


@router.post("/notify", tags=["external"])
def get_payment_url(order: OrderPointer, db: Session = Depends(get_db)):
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        raise HTTPException(404)
    payment_provider = PaymentServiceFactory.get_provider()
    status = payment_provider.get_payment_status(db_item)
    if status is not None and status != db_item.status:
        db_item.status = status
        db.commit()
        db.refresh(db_item)
    return Response()
