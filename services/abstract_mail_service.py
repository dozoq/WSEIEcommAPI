from abc import ABC, abstractmethod


class MailServiceProvider(ABC):

    @abstractmethod
    def send_email(self, order: dict) -> dict:
        pass