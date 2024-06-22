from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import models
from models.db import get_db
from models.dtos.emails_dtos import Email
from models.dtos.user_dtos import UserPointer, User
from services.factories.mail_service_factory import MailServiceFactory

router = APIRouter(
    prefix="/emails",
    tags=["emails"],
)


@router.post("/", response_model=None)
def send_email(email: Email, user: UserPointer, db: Session = Depends(get_db)) -> None:
    db_item = db.query(models.User).filter(models.User.id == user.id).first()
    if not db_item:
        raise HTTPException(status_code=400, detail="User not found")
    email_service = MailServiceFactory.get_provider()
    email_service.send_email(email.context, User.from_orm(db_item), email.template, email.subject)
    return