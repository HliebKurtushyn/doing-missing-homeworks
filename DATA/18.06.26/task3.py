import os
import time
import pandas as pd

# Збереження у Parquet
df_optimized.to_parquet("homework.parquet", index=False)

# Читання CSV
start = time.time()
csv_data = pd.read_csv("homework.csv")
csv_time = time.time() - start

# Читання Parquet
start = time.time()
parquet_data = pd.read_parquet("homework.parquet")
parquet_time = time.time() - start

# Використання пам'яті
csv_memory = csv_data.memory_usage(deep=True).sum() / 1024**2
parquet_memory = parquet_data.memory_usage(deep=True).sum() / 1024**2

print(f"CSV: {csv_time:.2f} с, {csv_memory:.2f} MB у пам'яті")
print(f"Parquet: {parquet_time:.2f} с, {parquet_memory:.2f} MB у пам'яті")

# Розмір файлів на диску
print(f"Розмір CSV: {os.path.getsize('homework.csv') / 1024**2:.2f} MB")
print(f"Розмір Parquet: {os.path.getsize('homework.parquet') / 1024**2:.2f} MB")