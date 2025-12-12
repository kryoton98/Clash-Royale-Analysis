from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from pathlib import Path
import joblib

from app.database import init_db
from app.api import deck, player, group
from app.ml.inference import InferenceService


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1) Init DB
    await init_db()

    # 2) Load model once and store on app.state
    models_dir = Path(__file__).resolve().parent / "ml" / "models"
    model_path = models_dir / "winrate_baseline.pkl"

    model_obj = joblib.load(model_path)
    model = model_obj["model"]

    app.state.inference_service = InferenceService(model=model, feature_engineer=None)

    yield

    # Optional: cleanup
    # del app.state.inference_service


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
