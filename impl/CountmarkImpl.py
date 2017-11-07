# _*_coding:utf-8_*_

# 计算学生成绩相关信息
# 计算学生的总成绩并进行排名
# 根据用户选择的科目进行单科排名
# 统计某一分段的学生数量(单科或总成绩,分段由用户输入)
# 用户可以输入学号来查询该学生的成绩信息及总成绩和单科成绩的排名
# 以上所有查到的信息,都显示科目的成绩等级

import pandas as pd
import config


class Countmark:
    def __init__(self):
        self.dataPath = config.PATH + '\database\\'
        self.file = self.dataPath + 'studentInfo.csv'
        self.coursesFile = self.dataPath + 'coursesInfo.csv'
        self.df = pd.read_csv(self.file, encoding='utf-8', dtype="str")
        self.coursesDf = pd.read_csv(self.coursesFile, encoding='utf-8', dtype="str")

    # 统计信息
    def getInfo(self):
        countDf = self.df.groupby(['studentId', 'name']).sum()
        allStudent = len(countDf)  # 总人数

        # 及格总数
        passDf = self.df[self.df.score >= '60']
        passRate = len(passDf) / (allStudent * 6)

        result = []
        # 课程信息
        dict = {}
        allDict = {}
        subjectDf = self.df.groupby(['subject']).sum()
        for i in subjectDf.index:
            oneDf = self.df[self.df.subject == i]
            onePassDf = oneDf[oneDf.score >= '60']
            detilTuple = (len(onePassDf), '%.2f%%' % ((len(onePassDf) / allStudent) * 100))
            dict[i] = detilTuple
        allDict['allStudent'] = allStudent
        allDict['passRate'] = '%.2f%%' % ((len(passDf) / (allStudent * 6)) * 100)
        allDict['detail'] = dict
        result.append(allDict)
        return allDict

    # 计算学生的总成绩并进行排名
    def getRanking(self):
        df = pd.read_csv(self.file)
        countDf = df.groupby(['studentId', 'name']).sum()
        sortCountDf = countDf.sort_values(['score'], ascending=False)  # 按顺序从大到小

        result = []

        for index, row in sortCountDf.iterrows():
            tupleResult = (index[0], index[1], str(row['score']))
            result.append(tupleResult)
        return result

    # 根据用户选择的科目进行单科排名
    def getOneRanking(self, subjectName):
        countDf = self.df[self.df.subject == subjectName]
        sortCountDf = countDf.sort_values(['score'], ascending=False)

        result = []

        for index, row in sortCountDf.iterrows():
            tupleResult = (row['name'], row['studentId'], row['subject'], row['score'])
            result.append(tupleResult)
        return result

    # 统计某一分段的学生数量(单科或总成绩,分段由用户输入)
    def getRegion(self, startScore, endScore, subject=None):
        result = []
        if subject is None:  # 没有选择科目，默认总成绩
            totalScore = self.df.groupby(['studentId', 'name']).sum()
            conditionDf = totalScore[
                (totalScore.score >= startScore) & (totalScore.score <= endScore)
                ]
            for index, row in conditionDf.iterrows():
                tupleResult = (index[0], index[1], row['score'])
                result.append(tupleResult)
        else:
            conditionDf = self.df[
                (self.df.score >= startScore) & (self.df.score <= endScore) & (self.df.subject == subject)
                ]
            for index, row in conditionDf.iterrows():
                tupleResult = (row['name'], row['studentId'], row['subject'], row['score'])
                result.append(tupleResult)
        # 统计人数
        studentNum = len(conditionDf)
        result.append(studentNum)

        return result

    # 用户可以输入学号来查询该学生的成绩信息及总成绩和单科成绩的排名
    def search(self, studentId):
        """
        dict = {
           'studentId' : 2017035101018,
           'name' : 刘爽,
           'totalScore' : 550,
           'totalRanking' : 2,
           'detailScore' : {
               'C语言': (88, 1),
               'Python': (88, 1),
               '安卓': (88, 1),
               '快速建站': (88, 1),
               'Linux': (88, 1),
               '网络': (88,1)
           }
        }
        """
        df = pd.read_csv(self.file)
        result = []
        dict = {}
        # 总成绩
        totalScore = df.groupby(['studentId', 'name']).sum()
        sortTotalScore = totalScore.sort_values(['score'], ascending=False)
        a = 0
        for index, item in sortTotalScore.iterrows():
            a += 1
            if index[0] == studentId:
                dict['studentId'] = studentId
                dict['name'] = index[1]
                dict['totalScore'] = str(item['score'])
                dict['totalRanking'] = a

        # 所有科目
        detailScore = {}
        allSubject = self.df.groupby(['subject']).sum()
        for index, item in allSubject.iterrows():
            oneSubjectScore = self.df[self.df.subject == index]
            sortOneScore = oneSubjectScore.sort_values(['score'], ascending=False)
            i = 0
            for id in sortOneScore['studentId']:
                i += 1
                if id == str(studentId):
                    oneSubjectTuple = (sortOneScore['score'].values[0], i)
                    detailScore[sortOneScore['subject'].values[0]] = oneSubjectTuple
        dict['detailScore'] = detailScore
        result.append(dict)
        return result

    # 以上所有查到的信息,都显示科目的成绩等级
    def showGrade(self):
        countDf = self.df.groupby(['studentId', 'name']).sum()
        allStudent = len(countDf)  # 总人数
        result = []
        # 课程信息

        allDict = {}
        subjectDf = self.df.groupby(['subject']).sum()
        grade = ['60', '75', '90']
        for i in subjectDf.index:
            dict = {}
            oneDf = self.df[self.df.subject == i]
            for j in grade:
                onePassDf = oneDf[oneDf.score >= j]
                detilTuple = (len(onePassDf), len(onePassDf) / allStudent)
                dict[j] = detilTuple
            allDict[i] = dict
        result.append(allDict)
        return allDict


if __name__ == '__main__':
    count = Countmark()
    # print(count.getRanking())  # 整体排名
    # print(count.getOneRanking("安卓")) #单科排名
    # count.getRegion(75, 76, subject='安卓') #统计某一分段成绩
    # print(count.showGrade())
    # print(count.search(2017035107140))
