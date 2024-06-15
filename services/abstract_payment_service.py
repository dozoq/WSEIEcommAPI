from abc import ABC, abstractmethod


class MailServiceProvider(ABC):

    @abstractmethod
    def get_payment_url(self, order: dict) -> dict:
        pass

    @abstractmethod
    def get_payment_status ( self, order: dict ) -> dict:
        pass