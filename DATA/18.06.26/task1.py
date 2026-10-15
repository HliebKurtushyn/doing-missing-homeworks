import pandas as pd

total_sum = 0
total_count = 0

for chunk in pd.read_csv("homework.csv", chunksize=10000):
    total_sum += chunk["Price"].sum()
    total_count += chunk["Price"].count()

average_price = total_sum / total_count if total_count else float("nan")

print(f"Середня ціна: {average_price:.2f}")