from abc import ABC, abstractmethod


class DeliveryServiceProvider(ABC):

    @abstractmethod
    def create_shipment(self, order: dict) -> dict:
        pass

    @abstractmethod
    def track_shipment(self, tracking_id: str) -> dict:
        pass

    @abstractmethod
    def cancel_shipment(self, tracking_id: str) -> dict:
        pass