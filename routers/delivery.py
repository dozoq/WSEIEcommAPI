from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.dtos.delivery_dtos import DeliveryResponse
from models.dtos.order_dtos import OrderPointer
from models.enums import OrderStatus
from models.models import Order
from services.factories.delivery_service_factory import DeliveryServiceFactory

router = APIRouter(
    prefix="/delivery",
    tags=["delivery"],
)


@router.get("/", response_model=DeliveryResponse)
def generate_tracking_number(order: OrderPointer, db: Session = Depends(get_db)):
    db_item: Order = db.query(Order).filter(Order.id == order.id).first()
    if db_item.status != OrderStatus.ORDER_PAID:
        return HTTPException(409)
    delivery_provider = DeliveryServiceFactory.get_provider()
    db_item.status = OrderStatus.ORDER_BEING_PACKED
    db.commit()
    db.refresh(db_item)
    return delivery_provider.generate_shipment_number()
