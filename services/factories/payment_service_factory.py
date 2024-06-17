from config import Settings
from services.abstract_payment_service import PaymentServiceProvider
from services.providers.mock_payment_service_impl import MockPaymentServiceProvider


class PaymentServiceFactory:

    @staticmethod
    def get_provider() -> PaymentServiceProvider:
        if Settings.PAYMENT_SERVICE_PROVIDER == MockPaymentServiceProvider.get_provider_name():
            return MockPaymentServiceProvider()
        else:
            raise ValueError(f"Unknown provider: {Settings.PAYMENT_SERVICE_PROVIDER}")

    @staticmethod
    def get_provider_by_name(name: str) -> PaymentServiceProvider:
        if name == MockPaymentServiceProvider.get_provider_name():
            return MockPaymentServiceProvider()
        else:
            raise ValueError(f"Unknown provider: {Settings.PAYMENT_SERVICE_PROVIDER}")