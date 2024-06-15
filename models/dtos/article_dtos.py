from pydantic import BaseModel


class ArticleGet(BaseModel):
    name: str
    description: str


class ArticleCreate(BaseModel):
    name: str
    description: str


class ArticleUpdate(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None


class ArticleDelete(BaseModel):
    id: int


class ArticleResponse(BaseModel):
    id: int
    name: str
    description: str