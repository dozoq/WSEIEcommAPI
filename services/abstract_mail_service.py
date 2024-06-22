from abc import ABC, abstractmethod

from models.dtos.user_dtos import User


class MailServiceProvider(ABC):

    @abstractmethod
    def send_email(self, context: dict, user: User, template: str, subject: str) -> None:
        pass
