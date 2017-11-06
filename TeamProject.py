from flask import Flask, json, jsonify
from impl.CountmarkImpl import Countmark
import pandas as pd
import numpy as np

app = Flask(__name__)
count = Countmark()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return "LOGIN"


@app.route('/')
def index():
    result = count.search('2017035101018')
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)
