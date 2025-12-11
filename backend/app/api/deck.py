from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import DeckEvaluateRequest, DeckEvaluateResponse

router = APIRouter()

@router.post("/evaluate", response_model=DeckEvaluateResponse)
async def evaluate_deck(request: DeckEvaluateRequest, db: AsyncSession = Depends(get_db)):
    return DeckEvaluateResponse(
        card_ids=request.card_ids,
        trophy_range=request.trophy_range,
        predicted_win_rate=0.55,
    )
