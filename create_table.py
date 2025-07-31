import sqlite3
conn=sqlite3.connect('ecommerce.db')
cursor=conn.cursor()
cursor.execute('''
               CREATE TABLE products(
                 id INTEGER PRIMARY KEY,cost REAL,category TEXT,name TEXT,brand TEXT,retail_price,department REAL,sku TEXT,distribution_center_id INTEGER
               )
               ''')
conn.commit()
conn.close()
print("Tablecretaed")