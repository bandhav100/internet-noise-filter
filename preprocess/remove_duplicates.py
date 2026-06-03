import pandas as pd

df = pd.read_json("data/merged_data.json")

print("Before:", len(df))

df = df.drop_duplicates(
    subset=["title"]
)

print("After:", len(df))

df.to_json(
    "data/final_dataset.json",
    orient="records",
    indent=4
)
