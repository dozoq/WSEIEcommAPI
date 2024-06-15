import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DELIVERY_SERVICE_PROVIDER: str = os.getenv("DELIVERY_SERVICE_PROVIDER")
    COMPANY_NAME: str = os.getenv("COMPANY_NAME")


settings = Settings()

