# _*_coding:utf-8_*_

# 创建两个csv文件(第一个CSV文件包括学号,姓名,科目,成绩信息（studentInfo）,第二个CSV文件包括科目,及格成绩,优等成绩,良等成绩(coursesInfo))

import pandas as pd
import numpy as np
import time, datetime, random, os, config


# from impl import config


class CreateCsv:
    def __init__(self):
        self.course = ['C语言', 'Python', '安卓', '快速建站', 'Linux', '网络']
        self.courLength = len(self.course)
        self.dataPath = config.PATH + '\database\\'

    def studentInfo(self, studentInfo):
        studentDf = pd.DataFrame({
            'studentId': np.array([studentInfo[1]] * self.courLength),
            'name': np.array([studentInfo[0]] * self.courLength),
            'subject': np.array(self.course),
            'score': np.array(
                [self.randomMark() for i in range(self.courLength)]),
        })
        fileName = self.dataPath + 'studentInfo1.csv'
        if os.path.exists(fileName):  # 存在
            header = False
        else:
            header = True
        studentDf.to_csv(self.dataPath + 'studentInfo1.csv', sep=',', encoding='utf-8', header=header, index=False,
                         mode='a+')

    def coursesInfo(self):
        coursesDf = pd.DataFrame({
            'subject': np.array(self.course),
            'passingScore': 60,
            'goodScore': 75,
            'excellentScore': 90
        })
        coursesDf.to_csv(self.dataPath + 'coursesInfo.csv', sep=',', encoding='utf-8', header=True, index=False)

    def createStudentId(self):
        today = datetime.date.today()
        year = today.year
        month = today.month
        day = today.day
        if len(str(day)) < 2:
            day = '0' + str(day)
        timeStamp = time.time()
        suffix = str(timeStamp)[-5:-1]
        return str(year) + str(month) + day + str(suffix)

    def randomMark(self):
        return random.randint(60, 100)

    def getStudentName(self):
        nameDf = pd.read_excel(self.dataPath + 'source.xls')
        tupleData = nameDf[['学号', '姓名']]
        studentInfo = []
        for index, row in tupleData.iterrows():
            tupleList = (row['学号'], row['姓名'])
            studentInfo.append(tupleList)
        return studentInfo


if __name__ == '__main__':
    createcsv = CreateCsv()
    studentInfo = createcsv.getStudentName()
    for i in studentInfo:
        createcsv.studentInfo(i)
        # createcsv.getStudentName()
