# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them).

%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('football.csv')
df = df.set_index(['Team'])
df["Goal Diff"] = abs(df["Goals"]-df["Goals Allowed"])

# List
#goal_diffs = df["Goal Diff"].value_counts

# Bar Chart
#df['Goal Diff'].plot(kind='bar', title ="For and Against",figsize=(15,10),legend=True, fontsize=12)

# Smallest Difference is the Aston_Villa Team
print( df["Goal Diff"].idxmin() )