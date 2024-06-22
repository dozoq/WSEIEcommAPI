import os

from dotenv import load_dotenv
import logging

load_dotenv()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DELIVERY_SERVICE_PROVIDER: str = os.getenv("DELIVERY_SERVICE_PROVIDER")
    PAYMENT_SERVICE_PROVIDER: str = os.getenv("PAYMENT_SERVICE_PROVIDER")
    MAIL_SERVICE_PROVIDER: str = os.getenv("MAIL_SERVICE_PROVIDER")
    COMPANY_NAME: str = os.getenv("COMPANY_NAME")
    SMTP_HOST: str = os.getenv("SMTP_HOST")
    SMTP_USER: str = os.getenv("SMTP_USER")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")
    SMTP_SENDER: str = os.getenv("SMTP_SENDER")


settings = Settings()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)