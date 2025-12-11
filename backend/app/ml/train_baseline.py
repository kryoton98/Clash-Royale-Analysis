import pandas as pd
import numpy as np
from pathlib import Path
from lightgbm import LGBMClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import joblib

PROJECT_ROOT = Path(__file__).resolve().parents[3]
BATTLES_SAMPLE = PROJECT_ROOT / "data" / "battles_sample.csv"

print("Loading battles sample...")
battles = pd.read_csv(BATTLES_SAMPLE)

# Make sure the expected columns exist
needed_cols = ["winner.elixir.average", "loser.elixir.average"]
missing = [c for c in needed_cols if c not in battles.columns]
if missing:
    raise ValueError(f"Missing columns in battles_sample.csv: {missing}")

# Build a symmetric dataset:
# Row 1: winner vs loser, label = 1
# Row 2: loser vs winner, label = 0
print("Building symmetric matchup dataset...")

df_win = pd.DataFrame({
    "a_elixir": battles["winner.elixir.average"].astype(float),
    "b_elixir": battles["loser.elixir.average"].astype(float),
})
df_win["elixir_diff"] = df_win["a_elixir"] - df_win["b_elixir"]
df_win["label"] = 1

df_lose = pd.DataFrame({
    "a_elixir": battles["loser.elixir.average"].astype(float),
    "b_elixir": battles["winner.elixir.average"].astype(float),
})
df_lose["elixir_diff"] = df_lose["a_elixir"] - df_lose["b_elixir"]
df_lose["label"] = 0

data = pd.concat([df_win, df_lose], ignore_index=True)
print(f"Total training rows: {len(data)}")

X = data[["a_elixir", "b_elixir", "elixir_diff"]].values
y = data["label"].values

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training LightGBM model...")
model = LGBMClassifier(
    objective="binary",
    n_estimators=200,
    learning_rate=0.05,
    num_leaves=31,
)
model.fit(X_train, y_train)

val_pred = model.predict_proba(X_val)[:, 1]
auc = roc_auc_score(y_val, val_pred)
print(f"Validation AUC: {auc:.3f}")

# Save model
models_dir = Path(__file__).resolve().parent / "models"
models_dir.mkdir(exist_ok=True)
model_path = models_dir / "winrate_baseline.pkl"
joblib.dump(
    {"model": model, "feature_names": ["a_elixir", "b_elixir", "elixir_diff"]},
    model_path,
)
print(f"Saved model to {model_path}")
