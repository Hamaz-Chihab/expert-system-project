from db.database import Base, engine
from fastapi import FastAPI
from routers.router import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
