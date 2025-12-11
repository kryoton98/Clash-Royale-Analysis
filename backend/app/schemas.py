from pydantic import BaseModel
from typing import List, Optional

class DeckEvaluateRequest(BaseModel):
    card_ids: List[str]
    trophy_range: str

class DeckEvaluateResponse(BaseModel):
    card_ids: List[str]
    trophy_range: str
    predicted_win_rate: float
