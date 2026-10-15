import time
import pandas as pd

CSV_PATH = "homework.csv"
PARQUET_PATH = "homework.parquet"


# Завдання 1: читання частинами
total_price = 0
price_count = 0

for chunk in pd.read_csv(CSV_PATH, chunksize=10000):
    total_price += chunk["Price"].sum()
    price_count += chunk["Price"].count()

average_price = total_price / price_count if price_count else float("nan")
print(f"Середня ціна: {average_price:.2f}")


# Завдання 2: оптимізація типів даних
start = time.perf_counter()
df = pd.read_csv(CSV_PATH)
default_time = time.perf_counter() - start
default_memory = df.memory_usage(deep=True).sum() / 1024**2

dtype_map = {}

for column in df.columns:
    series = df[column]

    if series.dtype == "object":
        if len(series) > 0 and series.nunique() / len(series) < 0.5:
            dtype_map[column] = "category"
    elif pd.api.types.is_integer_dtype(series):
        dtype_map[column] = pd.to_numeric(
            series, downcast="integer"
        ).dtype
    elif pd.api.types.is_float_dtype(series):
        dtype_map[column] = pd.to_numeric(
            series, downcast="float"
        ).dtype

start = time.perf_counter()
df_optimized = pd.read_csv(CSV_PATH, dtype=dtype_map)
optimized_time = time.perf_counter() - start
optimized_memory = df_optimized.memory_usage(deep=True).sum() / 1024**2

print("\nЗавдання 2: оптимізація dtype")
print(f"Час до оптимізації: {default_time:.3f} с")
print(f"Пам'ять до оптимізації: {default_memory:.2f} MiB")
print(f"Час після оптимізації: {optimized_time:.3f} с")
print(f"Пам'ять після оптимізації: {optimized_memory:.2f} MiB")


# Завдання 3: конвертація у Parquet
df_optimized.to_parquet(PARQUET_PATH, index=False)

start = time.perf_counter()
df_csv = pd.read_csv(CSV_PATH, dtype=dtype_map)
csv_time = time.perf_counter() - start
csv_memory = df_csv.memory_usage(deep=True).sum() / 1024**2

start = time.perf_counter()
df_parquet = pd.read_parquet(PARQUET_PATH)
parquet_time = time.perf_counter() - start
parquet_memory = df_parquet.memory_usage(deep=True).sum() / 1024**2

print("\nЗавдання 3: CSV vs Parquet")
print(f"CSV: читання {csv_time:.3f} с, пам'ять {csv_memory:.2f} MiB")
print(
    f"Parquet: читання {parquet_time:.3f} с, "
    f"пам'ять {parquet_memory:.2f} MiB"
)
print(f"Розмір CSV: {__import__('os').path.getsize(CSV_PATH) / 1024**2:.2f} MiB")
print(
    f"Розмір Parquet: "
    f"{__import__('os').path.getsize(PARQUET_PATH) / 1024**2:.2f} MiB"
)
