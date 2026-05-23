import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

sns.histplot(
    data=df,
    x='total_bill',
    bins=20,
    kde=True,
    color='brown',
    alpha=0.7,
    line_kws={'linewidth': 3}
)

plt.title('Розподіл Суми Рахунку з Налаштуваннями Графіка')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність')

plt.show()