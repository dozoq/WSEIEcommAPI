import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    PROVIDER_A_API_KEY: str = os.getenv("PROVIDER_A_API_KEY")
    PROVIDER_B_API_KEY: str = os.getenv("PROVIDER_B_API_KEY")


settings = Settings()

