import pandas as pd
import psycopg2

# الاتصال بقاعدة البيانات
conn = psycopg2.connect(
    dbname="ecommerce_nigeria",
    user="postgres",
    password="mot_de_passe_ici",
    host="localhost",
    port="5432"
)

# تحميل البيانات
df = pd.read_sql("SELECT * FROM sales", conn)

# حساب العمود الإجمالي
df["total"] = df["quantity"] * df["price"]

# التحليلات
total_revenue = df["total"].sum()
top_product = df.groupby("product")["quantity"].sum().idxmax()
top_customer = df.groupby("customer_id")["total"].sum().idxmax()

# عرض النتائج
print(" التحليل:")
print(f" إجمالي الأرباح: {total_revenue:.2f} نيرة")
print(f" أكثر منتج مبيعاً: {top_product}")
print(f"👤
 أفضل زبون: {top_customer}")

# إغلاق الاتصال
conn.close()

import pandas as pd
import psycopg2

# الاتصال بقاعدة البيانات
conn = psycopg2.connect(
    dbname="ecommerce_nigeria",
    user="postgres",
    password="mot_de_passe_ici",
    host="localhost",
    port="5432"
)

# تحميل البيانات
df = pd.read_sql("SELECT * FROM sales", conn)

# حساب العمود الإجمالي
df["total"] = df["quantity"] * df["price"]

# التحليلات
total_revenue = df["total"].sum()
top_product = df.groupby("product")["quantity"].sum().idxmax()
top_customer = df.groupby("customer_id")["total"].sum().idxmax()

# عرض النتائج
print(" التحليل:")
print(f" إجمالي الأرباح: {total_revenue:.2f} نيرة")
print(f" أكثر منتج مبيعاً: {top_product}")
print(f" أفضل زبون: {top_customer}")

# إغلاق الاتصال
conn.close()
