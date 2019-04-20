import pandas as pd

df = pd.read_json("../dangstagram_urls")

print(df.count())

keys = df[['key']]
print(keys.head(5))