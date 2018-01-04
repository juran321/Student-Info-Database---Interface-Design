#Ran Ju CESG 505
#Bonus Assignment
#class that get a connection between database and GUI

import sqlite3 as db

getType = '''
        SELECT * from Assignments
    '''

class DB(object):

    def __init__(self,database):
        self.database = database
        self.db = db.connect(self.database)
        self.db.text_factory = str
        self.cu = self.db.cursor()
    #get all assignment's name
    def getAss(self):
        self.cu.execute(getType)
        list = self.cu.fetchall()
        ass = []
        for i in list:
            if i[1] == 1:
                ass.append(i[2])
        return ass
    #get all lab's name
    def getLab(self):
        self.cu.execute(getType)
        list = self.cu.fetchall()
        lab = []
        for i in list:
            if i[1] == 2:
                lab.append(i[2])
        return lab
    #get all exam's name
    def getExam(self):
        self.cu.execute(getType)
        list = self.cu.fetchall()
        lab = []
        for i in list:
            if i[1] == 3 or i[1] == 4:
                lab.append(i[2])
        return lab
    #get all target score based on given assignment
    def getTarget(self):
        self.cu.execute(getType)
        list = self.cu.fetchall()
        d = {}
        for i in list:
            d[i[2]] = i[4]
        return d
    #get the number of row of Scores table
    def getCountScore(self):
        self.cu.execute('select count(*) from Scores' )
        list = self.cu.fetchall()
        return list[0][0]




