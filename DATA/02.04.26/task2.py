import pandas as pd

data = {
    'Product': ['Book', 'Pen', 'Notebook'],
    'Price': [15, 2, 5],
    'Stock': [100, 500, 200]
}

df = pd.DataFrame(data)

df['Discount'] = '10%'

df = df.drop(columns=['Stock'])

new_row = pd.DataFrame([{
    'Product': 'Pencil',
    'Price': 1,
    'Discount': '5%'
}])

df = pd.concat([df, new_row], ignore_index=True)

df = df.drop(index=1).reset_index(drop=True)

df['Supplier'] = 'Stationery Co.'

df = df.drop(index=2).reset_index(drop=True)

print(df)