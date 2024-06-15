from fastapi import FastAPI, Depends, HTTPException

from models.db import Base, engine
from routers import articles, users

app = FastAPI()




# Create tables
Base.metadata.create_all( bind=engine )

app.include_router(users.router)
app.include_router(articles.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}