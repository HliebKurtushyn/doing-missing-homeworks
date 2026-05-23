import pandas as pd

df_a = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Marketing']
})

df_b = pd.DataFrame({
    'EmployeeID': [4, 5],
    'Name': ['David', 'Eva'],
    'Department': ['Finance', 'IT']
})

combined = pd.concat([df_a, df_b], ignore_index=True)

multi = pd.concat([df_a, df_b], keys=['Group_A', 'Group_B'])

print(combined)
print(multi)