#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products


@app.route('/products')
def products():

    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()

        elif source == 'csv':
            data = read_csv()

        elif source == 'sql':
            data = read_sql()

        else:
            return render_template(
                'product_display.html',
                error='Wrong source',
                products=[]
            )

        if product_id:
            data = [
                product for product in data
                if str(product['id']) == product_id
            ]

            if not data:
                return render_template(
                    'product_display.html',
                    error='Product not found',
                    products=[]
                )

        return render_template(
            'product_display.html',
            products=data,
            error=None
        )

    except sqlite3.Error:
        return render_template(
            'product_display.html',
            error='Database error',
            products=[]
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
