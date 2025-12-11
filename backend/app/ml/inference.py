from typing import List

class InferenceService:
    def __init__(self, model, feature_engineer):
        self.model = model
        self.fe = feature_engineer
    
    def predict_matchup(self, deck_a: List[str], deck_b: List[str], trophy_range: str) -> float:
        return 0.55
