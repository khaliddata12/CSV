import pandas as pd
import psycopg2

# 1. تحميل البيانات من CSV
df = pd.read_csv("ecommerce_data.csv")

# تحويل التاريخ لتاريخ فعلي
df['order_date'] = pd.to_datetime(df['order_date'])

# 2. الاتصال بقاعدة البيانات
conn = psycopg2.connect(
    dbname="ecommerce_nigeria",
    user="postgres",
    password="mot_de_passe_ici",  # بدّلها بكلمة السر ديالك
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 3. إنشاء جدول جديد
cur.execute("""
    DROP TABLE IF EXISTS sales;
    CREATE TABLE sales (
        order_id INT PRIMARY KEY,
        customer_id TEXT,
        order_date DATE,
        product TEXT,
        quantity INT,
        price NUMERIC
    );
""")

# 4. إدخال البيانات
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO sales (order_id, customer_id, order_date, product, quantity, price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
print(" البيانات ترفعات بنجاح.")

# 5. حساب مجموع المبيعات الكلي
cur.execute("""
    SELECT ROUND(SUM(quantity * price), 2) FROM sales;
""")
total_sales = cur.fetchone()[0]
print(f" مجموع المبيعات الكلي: {total_sales} نيرة")

# 6. حساب معدل المبيعات الشهري
cur.execute("""
    SELECT TO_CHAR(order_date, 'YYYY-MM') AS month, 
           ROUND(SUM(quantity * price), 2) AS monthly_sales
    FROM sales
    GROUP BY month
    ORDER BY month;
""")
monthly_sales = cur.fetchall()
print("\n معدل المبيعات الشهري:")
for month, sales in monthly_sales:
    print(f"{month}: {sales} نيرة")

# 7. عدد الطلبات حسب كل منتج
cur.execute("""
    SELECT product, COUNT(*) AS num_orders
    FROM sales
    GROUP BY product
    ORDER BY num_orders DESC;
""")
product_orders = cur.fetchall()
print("\n عدد الطلبات حسب المنتج:")
for product, count in product_orders:
    print(f"{product}: {count} طلب")

# 8. إغلاق الاتصال
cur.close()
conn.close()
