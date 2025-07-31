import sqlite3
conn=sqlite3.connect('ecommerce.db')
cursor=conn.cursor()
cursor.execute("SELECT * FROM products LIMIT 5;")
rows=cursor.fetchall()
for row in rows :
  print(row)
  conn.close()
  print(" DATA VERIFY")