from flask import Flask, json, jsonify
from flask_cors import CORS
from impl.CountmarkImpl import Countmark
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app, supports_credentials=True)
count = Countmark()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return "LOGIN"


@app.route('/api/')
def index():
    result = count.search('2017035101018')
    return json.dumps(result)


@app.route('/api/getInfo')
def getInfo():
    studentInfo = count.getInfo()
    return json.dumps(studentInfo)


@app.route('/api/getCourseInfo')
def getCourseInfo():
    coursesInfo = count.showGrade()
    return json.dumps(coursesInfo)


@app.route('/api/getAllRank')
def getAllRank():
    allRank = count.getRanking()
    return json.dumps(allRank)


@app.route('/api/selectRank')
def SelectRank():
    subjectName = '安卓'
    selectRank = count.getOneRanking(subjectName)
    return json.dumps(selectRank)


if __name__ == '__main__':
    app.run(debug=True)
