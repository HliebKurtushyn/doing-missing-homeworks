import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

sns.histplot(
    data=df,
    x='total_bill',
    hue='smoker',
    bins=20,
    kde=True,
    element="step"
)

plt.title('Розподіл Суми Рахунку за Категорією Курців')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність')

plt.legend(title="Smoker")
plt.show()