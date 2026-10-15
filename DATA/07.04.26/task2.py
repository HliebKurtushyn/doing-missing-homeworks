import pandas as pd
import time

# Імпорт без оптимізації
start = time.time()
df = pd.read_csv("homework.csv")
normal_time = time.time() - start

normal_memory = df.memory_usage(deep=True).sum() / 1024**2

print(f"Час імпорту: {normal_time:.2f} с")
print(f"Використання пам'яті: {normal_memory:.2f} MB")

# Оптимізація числових типів і текстових стовпців
df_optimized = df.copy()

for col in df_optimized.columns:
    if pd.api.types.is_integer_dtype(df_optimized[col]):
        df_optimized[col] = pd.to_numeric(
            df_optimized[col], downcast="integer"
        )
    elif pd.api.types.is_float_dtype(df_optimized[col]):
        df_optimized[col] = pd.to_numeric(
            df_optimized[col], downcast="float"
        )
    elif df_optimized[col].dtype == "object":
        if df_optimized[col].nunique() / max(len(df_optimized), 1) < 0.5:
            df_optimized[col] = df_optimized[col].astype("category")

start = time.time()
df_optimized.to_csv("homework_optimized.csv", index=False)
optimized_time = time.time() - start

optimized_memory = (
    df_optimized.memory_usage(deep=True).sum() / 1024**2
)

print(f"Пам'ять після оптимізації: {optimized_memory:.2f} MB")
print(f"Зменшення пам'яті: {normal_memory - optimized_memory:.2f} MB")
print(f"Час збереження оптимізованих даних: {optimized_time:.2f} с")
print(df_optimized.dtypes)