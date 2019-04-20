import pandas as pd

df = pd.read_json("../dangstagram_urls")

print(df.count())


print(df.head(5))

