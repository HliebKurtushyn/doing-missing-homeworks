import pandas as pd
import numpy as np
import time

np.random.seed(0)

transactions_df = pd.DataFrame({
    'TransactionID': range(1, 100001),
    'UserID': np.random.randint(1, 1001, size=100000),
    'ProductID': np.random.randint(1, 500, size=100000),
    'Date': pd.date_range('2023-01-01', periods=100000, freq='min'),
    'Amount': np.random.uniform(10, 1000, size=100000)
})

transactions_df['Amount'] = transactions_df['Amount'].astype('float32')
transactions_df = transactions_df.set_index(['UserID', 'ProductID'])

products_df = pd.DataFrame({
    'ProductID': np.arange(1, 500),
    'Category': np.random.choice(['A', 'B', 'C'], 499)
})

t1 = time.time()
merge_slow = transactions_df.reset_index().merge(products_df, on='ProductID')
t2 = time.time()

t3 = time.time()
merge_fast = transactions_df.reset_index().merge(products_df, on='ProductID')
t4 = time.time()

print("Slow:", t2 - t1)
print("Fast:", t4 - t3)