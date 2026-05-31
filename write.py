import pandas as pd
from sklearn.model_selection import train_test_split
import json

# ======================
# 1. LOAD DATA
# ======================
df = pd.read_csv("data.csv")

# ======================
# 2. CREATE STABLE ID
# ======================
df = df.reset_index(drop=True)
df["id"] = df.index.astype(int)

# đảm bảo không bị NaN label
df = df.dropna(subset=["label"]).reset_index(drop=True)

# ======================
# 3. SPLIT DATA
# ======================
train_df, temp_df = train_test_split(
    df,
    test_size=0.3,
    random_state=42,
    stratify=df["label"]
)

val_df, test_df = train_test_split(
    temp_df,
    test_size=0.5,
    random_state=42,
    stratify=temp_df["label"]
)

# ======================
# 4. SAVE DATA WITH ID
# ======================
df.to_csv("data_with_id.csv", index=False)

train_df.to_csv("train.csv", index=False)
val_df.to_csv("val.csv", index=False)
test_df.to_csv("test.csv", index=False)

# ======================
# 5. SAVE SPLIT JSON (ONLY IDS)
# ======================
splits = {
    "train": train_df["id"].tolist(),
    "val": val_df["id"].tolist(),
    "test": test_df["id"].tolist()
}

with open("split.json", "w", encoding="utf-8") as f:
    json.dump(splits, f, ensure_ascii=False, indent=2)

print("✅ Done: data_with_id.csv + train/val/test + split.json")