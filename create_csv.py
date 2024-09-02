import pandas as pd
import json

with open("professor_info.txt", "r") as f:
    data = json.load(f)

df = pd.json_normalize(data)

df.to_csv("research_data.csv", index=False)
