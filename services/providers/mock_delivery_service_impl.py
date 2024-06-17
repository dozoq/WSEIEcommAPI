import string
from abc import ABC
from random import random

from config import Settings
from models.dtos.delivery_dtos import DeliveryResponse
from models.dtos.order_dtos import OrderPointer
from models.enums import OrderStatus
from services.abstract_delivery_service import DeliveryServiceProvider


class MockDeliveryServiceProvider(DeliveryServiceProvider, ABC):
    orders_updated: list = []


    @staticmethod
    def get_provider_name() -> str:
        return "mock"

    def generate_shipment_number(self, order: OrderPointer) -> DeliveryResponse:
        response: DeliveryResponse = DeliveryResponse(
            package_name=f"Package {order.id} from {Settings.COMPANY_NAME}",
            tracking_number=''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            delivery_provider=self.get_provider_name())
        return response

    def unpack_shipment_status(self, order: OrderPointer) -> OrderStatus:
        if not MockDeliveryServiceProvider.orders_updated.__contains__(order.id):
            MockDeliveryServiceProvider.orders_updated.append(order.id)
            return OrderStatus.ORDER_SENT
        else:
            return OrderStatus.ORDER_DELIVERED
