import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('penguins')
df = df.dropna()
df_encoded = df.copy()

for col in df_encoded.select_dtypes(include='object').columns:
    df_encoded[col] = df_encoded[col].astype('category').cat.codes

corr = df_encoded.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title('Кореляційна матриця (з категоріями)')
plt.show()