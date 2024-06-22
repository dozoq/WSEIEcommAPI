from config import Settings
from services.abstract_mail_service import MailServiceProvider
from services.providers.SMTP_mail_service_provider_impl import SMTPMailServiceProvider
from services.providers.mock_mail_service_provider_impl import MockMailServiceProvider


class MailServiceFactory:

    @staticmethod
    def get_provider() -> MailServiceProvider:
        if Settings.MAIL_SERVICE_PROVIDER == MockMailServiceProvider.get_provider_name():
            return MockMailServiceProvider()
        if Settings.MAIL_SERVICE_PROVIDER == SMTPMailServiceProvider.get_provider_name():
            return SMTPMailServiceProvider()
        else:
            raise ValueError(f"Unknown provider: {Settings.MAIL_SERVICE_PROVIDER}")

    @staticmethod
    def get_provider_by_name(name: str) -> MailServiceProvider:
        if name == MockMailServiceProvider.get_provider_name():
            return MockMailServiceProvider()
        if name == SMTPMailServiceProvider.get_provider_name():
            return SMTPMailServiceProvider()
        else:
            raise ValueError(f"Unknown provider: {Settings.MAIL_SERVICE_PROVIDER}")