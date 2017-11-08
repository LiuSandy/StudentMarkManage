from flask import Flask, json, jsonify, request
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
    subjectName = request.args.get('q')
    selectRank = count.getOneRanking(subjectName)
    return json.dumps(selectRank)


@app.route('/api/getDetail')
def getDetail():
    studentId = request.args.get('q')
    detail = count.search(int(studentId))
    return json.dumps(detail)


@app.route('/api/getRegion')
def getRegion():
    startScore = request.args.get('startScore')
    endScore = request.args.get('endScore')
    subject = request.args.get('subject')
    result = count.getRegion(startScore, endScore, subject)
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)
