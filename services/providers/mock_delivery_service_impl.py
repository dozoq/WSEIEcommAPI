from services.abstract_delivery_service import DeliveryServiceProvider


class MockDeliveryServiceProvider(DeliveryServiceProvider):

    def create_shipment(self, data: dict) -> dict:
        # Implementation for Provider A
        pass

    def track_shipment(self, tracking_id: str) -> dict:
        # Implementation for Provider A
        pass

    def cancel_shipment(self, tracking_id: str) -> dict:
        # Implementation for Provider A
        pass