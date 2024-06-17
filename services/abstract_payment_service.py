from abc import ABC, abstractmethod

from models.dtos.order_dtos import OrderPointer
from models.enums import OrderStatus


class PaymentServiceProvider(ABC):

    @abstractmethod
    def get_payment_url(self, order: OrderPointer) -> str:
        pass

    @abstractmethod
    def get_payment_status(self, order: OrderPointer) -> OrderStatus:
        pass
