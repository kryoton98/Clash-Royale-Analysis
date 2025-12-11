from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from app.database import init_db
from app.api import deck, player, group

async def startup():
    await init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield

app = FastAPI(title="Clash Royale Deck Brain", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deck.router, prefix="/api/deck", tags=["deck"])
app.include_router(player.router, prefix="/api/player", tags=["player"])
app.include_router(group.router, prefix="/api/group", tags=["group"])

@app.get("/health")
async def health():
    return {"status": "ok"}
