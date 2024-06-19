from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine
from contextlib import asynccontextmanager


metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    
    yield
    
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(movies)

