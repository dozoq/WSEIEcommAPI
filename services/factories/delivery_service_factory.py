from config import Settings
from services.abstract_delivery_service import DeliveryServiceProvider
from services.providers.mock_delivery_service_impl import MockDeliveryServiceProvider


class DeliveryServiceFactory:

    @staticmethod
    def get_provider() -> DeliveryServiceProvider:
        if Settings.DELIVERY_SERVICE_PROVIDER == MockDeliveryServiceProvider.get_provider_name():
            return MockDeliveryServiceProvider()
        else:
            raise ValueError(f"Unknown provider: {Settings.DELIVERY_SERVICE_PROVIDER}")

    @staticmethod
    def get_provider_by_name(name: str) -> DeliveryServiceProvider:
        if name == MockDeliveryServiceProvider.get_provider_name():
            return MockDeliveryServiceProvider()
        else:
            raise ValueError(f"Unknown provider: {Settings.DELIVERY_SERVICE_PROVIDER}")
