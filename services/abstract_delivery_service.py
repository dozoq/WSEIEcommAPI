from abc import ABC, abstractmethod

from models.dtos.order_dtos import OrderPointer


class DeliveryServiceProvider(ABC):

    @abstractmethod
    def generate_shipment_number(self, order: OrderPointer) -> dict:
        pass

    @abstractmethod
    def ask_for_shipment(self, order: OrderPointer) -> None:
        pass

    @abstractmethod
    def unpack_shipment_status(self, order: OrderPointer, shipment_response) -> None:
        pass
