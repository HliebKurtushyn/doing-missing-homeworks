import matplotlib.pyplot as plt

weeks = ['Тиждень 1', 'Тиждень 2', 'Тиждень 3', 'Тиждень 4']

traffic = [1500, 1600, 1700, 1800]

sales_product_a = [300, 350, 400, 450]
sales_product_b = [200, 250, 300, 350]
sales_product_c = [100, 150, 200, 250]

plt.plot(weeks, traffic, label="Traffic", color="black", linestyle="-")

plt.plot(weeks, sales_product_a, label="Product A", color="red", linestyle="--")
plt.plot(weeks, sales_product_b, label="Product B", color="blue", linestyle=":")
plt.plot(weeks, sales_product_c, label="Product C", color="green", linestyle="-.")

plt.title("Traffic vs Sales")
plt.xlabel("Weeks")
plt.ylabel("Values")
plt.legend()

plt.show()