import psycopg2

conn = psycopg2.connect(
    dbname="pizzeria_db",
    user="postgres",
    password="300911",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    SELECT COUNT(*)
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '1 month';
""")

print("Замовлень за місяць:", cur.fetchone()[0])


cur.execute("""
    SELECT m.name, SUM(oi.quantity) AS total
    FROM order_items oi
    JOIN menu m ON m.id = oi.menu_id
    GROUP BY m.name
    ORDER BY total DESC
    LIMIT 1;
""")


print("Топ страва:", cur.fetchone())

cur.execute("""
    SELECT AVG(total_price)
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '3 months';
""")

print("Середній чек:", cur.fetchone()[0])


conn.close()