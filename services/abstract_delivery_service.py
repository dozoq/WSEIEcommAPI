from abc import ABC, abstractmethod

from models.dtos.order_dtos import OrderPointer
from models.enums import OrderStatus


class DeliveryServiceProvider(ABC):

    @abstractmethod
    def generate_shipment_number(self, order: OrderPointer) -> dict:
        pass

    @abstractmethod
    def unpack_shipment_status(self, order: OrderPointer) -> OrderStatus:
        pass
