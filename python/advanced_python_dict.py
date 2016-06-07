import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.columns = df.columns.str.strip()
df.rename(columns=lambda x: x.strip())
df["fn"], df["ln"] = zip(*df["name"].str.split().tolist())
del df["name"]
df = df[['fn', 'ln', 'degree', 'title', 'email']]

dict = df.set_index(['ln','fn']).T.to_dict('list')
print(dict)