import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.columns = df.columns.str.strip()
df.rename(columns=lambda x: x.strip())
df["domain"] = df["email"].apply(lambda x: x.split('@')[1])
df["domain"].value_counts()

df['email'].to_csv('faculty_email.csv', index=False, encoding='utf-8')