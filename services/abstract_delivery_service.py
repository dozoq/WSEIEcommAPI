from abc import ABC, abstractmethod

from models.dtos.order_dtos import OrderPointer


class DeliveryServiceProvider(ABC):

    @abstractmethod
    def generate_shipment_number(self, order: OrderPointer) -> dict:
        pass