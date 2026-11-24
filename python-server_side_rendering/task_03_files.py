#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


@app.route('/products')
def products():

    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()

    elif source == 'csv':
        data = read_csv()

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
