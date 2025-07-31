import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Open the CSV file
with open('products.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Extract relevant fields (adjust based on your actual CSV columns)
        id = row.get('id')
        cost = row.get('cost')
        category = row.get('category')
        brand = row.get('brand')
        name=row.get('name')
        retail_price = row.get('retail_price')
        department = row.get('department')
        sku = row.get('sku')
        distribution_center_id = row.get('distribution_center_id')

        # Insert into database
        cursor.execute('''
            INSERT INTO products (id, cost, category, brand,name, retail_price, department, sku, distribution_center_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id, cost, category, brand, name,retail_price, department, sku, distribution_center_id))

# Commit and close
conn.commit()
conn.close()

print("✅ Data loaded successfully.")
