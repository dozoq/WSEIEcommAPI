from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from models.db import get_db
from models.dtos.article_dtos import ArticleResponse, ArticleCreate, ArticleUpdate, ArticleDelete
from models.models import Article

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items(db: Session = Depends(get_db)):
    return db.query(Article).all()


@router.get("/{item_id}", response_model=List[ArticleResponse])
async def read_item(item_id: str, db: Session = Depends(get_db)) -> List[ArticleResponse]:
    db_item: Article = db.query(Article).filter(Article.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.post("/", response_model=ArticleResponse)
async def create_item(item: ArticleCreate, db: Session = Depends(get_db)) -> ArticleResponse:
    db_item: Article = Article(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.patch("/", response_model=ArticleResponse)
async def update_item(item: ArticleUpdate, db: Session = Depends(get_db)) -> ArticleResponse:
    db_item: Article = db.query(Article).filter(Article.id == item.id).first()
    db_item.name = item.name if item.name is not None else db_item.name
    db_item.description = item.description if item.description is not None else db_item.description
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/", response_model=None)
async def delete_item(item: ArticleDelete, db: Session = Depends(get_db)) -> None:
    db_item: Article = db.query(Article).filter(Article.id == item.id).first()
    db.delete(db_item)
    db.commit()
    return
