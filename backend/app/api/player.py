from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.post("/analyze")
async def analyze_player(request: dict, db: AsyncSession = Depends(get_db)):
    return {"player_tag": request.get("player_tag"), "trophies": 5000}

@router.post("/recommend_decks")
async def recommend_decks(request: dict, db: AsyncSession = Depends(get_db)):
    return {"decks": []}
