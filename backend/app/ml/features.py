import numpy as np
from typing import List, Dict

class FeatureEngineer:
    def __init__(self, card_data: Dict[str, Dict]):
        self.card_data = card_data
    
    def get_deck_features(self, card_ids: List[str]) -> Dict[str, float]:
        features = {}
        cards = [self.card_data.get(cid, {}) for cid in card_ids]
        elixirs = [c.get("elixir_cost", 0) for c in cards]
        features["avg_elixir"] = np.mean(elixirs) if elixirs else 0
        features["min_elixir"] = np.min(elixirs) if elixirs else 0
        features["max_elixir"] = np.max(elixirs) if elixirs else 0
        return features
