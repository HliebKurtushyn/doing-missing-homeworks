import pandas as pd

data = {
    'Name': ['Alex', 'Bella', 'Chris'],
    'Age': [30, 25, 35],
    'City': ['Kyiv', 'Lviv', 'Odesa']
}
df = pd.DataFrame(data)

df['Salary'] = [50000, 60000, 55000]

df = df.drop(columns=['Age'])

new_row = pd.DataFrame([{
    'Name': 'Diana',
    'City': 'Dnipro',
    'Salary': 58000
}])

df = pd.concat([df, new_row], ignore_index=True)

df = df.drop(index=0).reset_index(drop=True)

df['Department'] = 'Sales'

df = df.drop(columns=['Salary'])

print(df)