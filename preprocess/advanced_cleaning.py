import pandas as pd
import re
#loadin the data sett...
df=pd.read_csv("data/cleaned_hackernews.csv")
print("orginal titles :\n")
print(df["title"].head())

#text cleaning function
def clean_text(text):
    text=text.lower() #convert into lowercase
    text= re.sub(r'[^a-zA-Z0-9\s]','',text)
    text=re.sub(r'\s+',' ',text).strip()
    return text
df["clean_title"] = df["title"].astype(str).apply(clean_text)

print("\nCleaned Titles:\n")

print(df["clean_title"].head())

# Save processed data
df.to_csv("data/processed_hackernews.csv", index=False)

print("\nAdvanced cleaned data saved!")
