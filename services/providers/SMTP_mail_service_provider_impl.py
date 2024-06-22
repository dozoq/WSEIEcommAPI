import smtplib
from abc import ABC
from email.mime.text import MIMEText

from config import Settings
from models.dtos.user_dtos import User
from services.abstract_mail_service import MailServiceProvider
from services.utility.template_reader import render_template


class SMTPMailServiceProvider(MailServiceProvider, ABC):

    @staticmethod
    def get_provider_name() -> str:
        return "email_labs"

    def send_email(self, context: dict, user: User, template: str, subject: str) -> str:
        msg = MIMEText(render_template(template, context), 'html')
        msg['Subject'] = subject
        msg['From'] = Settings.SMTP_SENDER
        msg['To'] = user.email

        with smtplib.SMTP(Settings.SMTP_HOST, 587) as server:
            server.login(Settings.SMTP_USER, Settings.SMTP_PASSWORD)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())