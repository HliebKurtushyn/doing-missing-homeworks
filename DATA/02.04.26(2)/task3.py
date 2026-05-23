import pandas as pd

df = pd.read_csv("customer_feedback.csv")

grouped = df.groupby(['Region', 'Month'])['Rating'].mean()
wide = grouped.unstack()
wide = wide.fillna(wide.stack().mean())

print(wide)