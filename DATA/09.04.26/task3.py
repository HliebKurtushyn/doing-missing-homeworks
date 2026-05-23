import matplotlib.pyplot as plt

sizes = [50, 25, 15, 10]
labels = ['Продажі', 'Інвестиції', 'Ліцензії', 'Інше']

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

plt.pie(sizes, labels=labels, colors=colors)
plt.title("Кольори сегментів")

plt.show()