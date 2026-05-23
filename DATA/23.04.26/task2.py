import pandas as pd

orders_df = pd.DataFrame({
    'OrderID': [1001, 1002, 1003, 1004],
    'CustomerID': [1, 2, 1, 3],
    'ProductID': [501, 502, 503, 504],
    'Quantity': [2, 1, 5, 3]
})

customers_df = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

merged = orders_df.merge(customers_df, on='CustomerID', how='inner')

merged_multi = orders_df.merge(
    customers_df,
    on='CustomerID',
    how='inner',
    indicator=True
)

print(merged)
print(merged_multi)