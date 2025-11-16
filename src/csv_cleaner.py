import pandas as pd

def clean_csv(path):
    df = pd.read_csv(path)
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    df.to_csv("cleaned_output.csv", index=False)
    print("Cleaned file saved: cleaned_output.csv")
