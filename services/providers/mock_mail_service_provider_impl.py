from abc import ABC

from config import logger
from models.dtos.user_dtos import User
from services.abstract_mail_service import MailServiceProvider
from services.utility.template_reader import render_template


class MockMailServiceProvider(MailServiceProvider, ABC):

    @staticmethod
    def get_provider_name() -> str:
        return "mock"

    def send_email(self, context: dict, user: User, template: str, subject: str) -> str:
        email_content = render_template(template, context)
        logger.info(f"Email Sent To {user.email} subject:{subject} with {email_content}")
        return {"message": "Email sent successfully"}
