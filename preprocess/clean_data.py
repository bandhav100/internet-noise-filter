import json
import pandas as pd

# Load JSON data
with open("data/hackernews.json", "r") as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

print("\n" + "="*50)

# Remove missing titles
df = df.dropna(subset=["title"])

# Remove duplicate titles
df = df.drop_duplicates(subset=["title"])

print("\nCleaned Data:\n")
print(df)

# Save cleaned CSV
df.to_csv("data/cleaned_hackernews.csv", index=False)

print("\nCleaned data saved successfully!")
