from fastapi import APIRouter, HTTPException, Request
from app.schemas import DeckEvaluateRequest, DeckEvaluateResponse

router = APIRouter()


@router.post("/evaluate", response_model=DeckEvaluateResponse)
async def evaluate_deck(request: Request, body: DeckEvaluateRequest) -> DeckEvaluateResponse:
    # Access the service without importing app.main (avoids circular import)
    svc = getattr(request.app.state, "inference_service", None)
    if svc is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    a = float(body.avg_elixir)
    b = float(body.opponent_avg_elixir)
    elixir_diff = a - b

    X = [[a, b, elixir_diff]]
    win_prob = float(svc.model.predict_proba(X)[0, 1])

    return DeckEvaluateResponse(
        win_probability=win_prob,
        features={"a_elixir": a, "b_elixir": b, "elixir_diff": elixir_diff},
    )
