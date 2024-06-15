from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.db import get_db
from models.dtos.user_dtos import UserResponse, UserCreate, UserUpdate, UserDelete
from models.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/{username}", response_model=UserResponse)
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    return db.query(User).filter(User.username == username).first()


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_item: User = User(**user.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.patch("/", response_model=UserResponse)
def update_user(user: UserUpdate, db: Session = Depends(get_db)):
    db_item: User = db.query(User).filter(User.id == user.id).first()
    db_item.first_name = user.first_name if user.first_name is not None else db_item.first_name
    db_item.last_name = user.last_name if user.last_name is not None else db_item.last_name
    db_item.username = user.username if user.username is not None else db_item.username
    db_item.password = user.password if user.password is not None else db_item.password
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/", response_model=None)
async def delete_user(user: UserDelete, db: Session = Depends(get_db)) -> None:
    db_item: User = db.query(User).filter(User.id == user.id).first()
    db.delete(db_item)
    db.commit()
    return
