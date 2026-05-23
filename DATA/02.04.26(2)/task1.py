import pandas as pd

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}

df = pd.DataFrame(data)

new_row = pd.DataFrame([{
    'Product': 'USB Hub',
    'Price': 40,
    'Stock': 150,
    'Warranty': '2 years'
}])

df = pd.concat([df, new_row], ignore_index=True)

print(df)