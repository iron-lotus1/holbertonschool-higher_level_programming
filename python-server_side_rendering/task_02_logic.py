#!/usr/bin/env python3

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

    items = data.get('items', [])

    return render_template('items.html', items=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
