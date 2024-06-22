from pydantic import BaseModel


class Email(BaseModel):
    template: str
    subject: str
    context: dict | None = None
