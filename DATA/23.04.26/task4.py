import pandas as pd

df_sales = pd.DataFrame({
    'SaleID': [2001, 2002, 2003, 2004, 2005],
    'StoreID': [10, 20, 10, 30, 20],
    'ProductID': [301, 302, 303, 301, 304],
    'UnitsSold': [50, 60, 70, 80, 90]
})

df_suppliers = pd.DataFrame({
    'SupplierID': [401, 402, 403, 404],
    'ProductID': [301, 302, 303, 305],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
})

df_sales = df_sales.set_index(['StoreID', 'ProductID'])

merged = df_sales.reset_index().merge(
    df_suppliers,
    on='ProductID',
    how='left',
    validate='many_to_one',
    suffixes=('_sale', '_supplier')
)

print(merged)