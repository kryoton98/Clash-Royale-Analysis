from pydantic import BaseModel, Field


class DeckEvaluateRequest(BaseModel):
    avg_elixir: float = Field(..., ge=0.0, le=10.0)
    opponent_avg_elixir: float = Field(4.0, ge=0.0, le=10.0)


class DeckEvaluateResponse(BaseModel):
    win_probability: float = Field(..., ge=0.0, le=1.0)
    features: dict[str, float]
