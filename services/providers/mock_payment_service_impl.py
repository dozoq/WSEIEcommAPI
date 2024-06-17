from abc import ABC

from models.dtos.order_dtos import OrderPointer
from models.enums import OrderStatus
from services.abstract_payment_service import PaymentServiceProvider


class MockPaymentServiceProvider(PaymentServiceProvider, ABC):
    orders_updated: list = []

    @staticmethod
    def get_provider_name() -> str:
        return "mock"

    def get_payment_url(self, order: OrderPointer) -> str:
        return r"https://www.google.com"

    def get_payment_status(self, order: OrderPointer) -> OrderStatus:
        return OrderStatus.ORDER_PAID
