# Copy/Pasta from Jupyter
# Gist Link: https://gist.github.com/a6944bf506d7be814ea1191ee33da755
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.columns = df.columns.str.strip()
df.rename(columns=lambda x: x.strip())

df["domain"] = df["email"].apply(lambda x: x.split('@')[1])
df["domain"].value_counts()

# more verbose
#extract_domain = lambda x: x.split('@')[1]
#df["domain"] = df["email"].apply(extract_domain)