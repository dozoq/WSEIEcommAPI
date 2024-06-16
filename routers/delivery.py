from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from models.db import get_db
from models.dtos.delivery_dtos import DeliveryResponse
from models.dtos.order_dtos import OrderPointer, OrderResponse
from models.enums import OrderStatus
from models.models import Order
from services.factories.delivery_service_factory import DeliveryServiceFactory

router = APIRouter(
    prefix="/delivery",
)


@router.post("/", tags=["delivery"], response_model=DeliveryResponse)
def generate_tracking_number(order: OrderPointer, db: Session = Depends(get_db)):
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None or db_item.status != OrderStatus.ORDER_PAID:
        raise HTTPException(409)
    delivery_provider = DeliveryServiceFactory.get_provider()
    db_item.status = OrderStatus.ORDER_BEING_PACKED
    db.commit()
    db.refresh(db_item)
    return delivery_provider.generate_shipment_number(order)


@router.patch("/", tags=["external"], response_model=None)
def update_shipment_status(order: OrderPointer, db: Session = Depends(get_db)):
    """External endpoint for delivery providers"""
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item is None:
        raise HTTPException(409, detail={"error": "ORDER_NOT_FOUND"})
    delivery_provider = DeliveryServiceFactory.get_provider()
    status = delivery_provider.unpack_shipment_status(db_item, "")
    if status is not None and status != db_item.status:
        db_item.status = status
        db.commit()
        db.refresh(db_item)
    return Response()
