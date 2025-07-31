from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)
DATABASE = 'products.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dict-like objects
    return conn

@app.route('/api/products', methods=['GET'])
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    result = [dict(row) for row in products]
    return jsonify(result)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
    product = cursor.fetchone()
    conn.close()

    if product is None:
        abort(404, description="Product not found")

    return jsonify(dict(product))

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
