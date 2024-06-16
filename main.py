from fastapi import FastAPI, Depends, HTTPException

from models.db import Base, engine
from routers import articles, users, orders, delivery

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(articles.router)
app.include_router(orders.router)
app.include_router(delivery.router)