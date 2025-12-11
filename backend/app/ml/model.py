import numpy as np
from typing import List

class WinRateModel:
    def __init__(self):
        self.model = None
        self.feature_names = None
    
    def train(self, X_train: np.ndarray, y_train: np.ndarray, feature_names: List[str]):
        self.feature_names = feature_names
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return np.random.rand(len(X))
