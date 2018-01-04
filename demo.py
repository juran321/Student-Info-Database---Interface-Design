import sys
from PyQt5.QtWidgets import *
import sqlite3 as db
import database

d = database.DB('Scores.db')
list1 = d.getAss()
list2 = d.getLab()
list3 = d.getExam()
class CollectScores(QWidget):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(CollectScores, self).__init__()

        self.initUI()

    def initUI(self):
        list = list1
        label_1 = QLabel('Name:', self)
        label_1.move(0,0)
        table_1 = QTableWidget(self)
        table_1.move(0,100)
        target = QLabel('Target:',self)
        target.move(300,300)
        score = QLabel('Score:',self)
        score.move(300,330)
        box = QGroupBox('Type',self)
        radio1 = QRadioButton('HW',self)
        radio2 = QRadioButton('Lab',self)
        radio3 = QRadioButton('Exams',self)
        radio2.setChecked(True)
        vbox = QGridLayout()
        vbox.addWidget(radio1,0,0)
        vbox.addWidget(radio2,0,1)
        vbox.addWidget(radio3,0,2)
        box.setLayout(vbox)
        box.move(300,0)

        radio1.clicked.connect(self.selectionchange1)
        radio2.clicked.connect(self.selectionchange2)
        radio3.clicked.connect(self.selectionchange3)
        combobox = QComboBox()
        combobox.move(20, 120)
        combobox.addItems(list1)



        le_name = QLineEdit(self)
        le_name.move(100,0)
        le_target = QLineEdit(self)
        le_target.move(350,300)
        le_score = QLineEdit(self)
        le_score.move(350,330)


        pbtn_cancel = QPushButton('cancel', self)
        pbtn_save = QPushButton('save', self)
        pbtn_cancel.move(300,380)
        pbtn_save.move(400,380)

        # lyt = QGridLayout()
        # lyt.addWidget(label_1, 0, 0)
        # lyt.addWidget(le_name, 0, 1)
        # lyt.addWidget(table_1,1,0)
        #
        # lyt.addWidget(self.createGourp(), 0, 3)
        # lyt.addWidget(cbx_assignment,1,3)
        # lyt.addWidget(self.createGroup2(),4,3)
        # lyt.addWidget(target,4,3)
        # lyt.addWidget(le_target,4,4)
        # lyt.addWidget(score,5,3)
        # lyt.addWidget(le_score,5,4)

        # lyt.addWidget(pbtn_cancel, 6, 3)
        # lyt.addWidget(pbtn_save, 6, 4)
        self.setGeometry(500, 500, 550, 450)
        self.setWindowTitle('Main Windows')
        self.show()
        # self.setLayout(lyt)
        #
        # self.show()
    def selectionchange1(self,i):
        self.combobox.clear()
        self.combobox.addItems(list1)
    def selectionchange2(self,i):
        self.combobox.clear()
        self.combobox.addItems(list2)
    def selectionchange3(self,i):
        self.combobox.clear()
        self.combobox.addItems(list3)


    def createGourp(self):
        box = QGroupBox('Type')
        radio1 = QRadioButton('HW')
        radio2 = QRadioButton('Lab')
        radio3 = QRadioButton('Exams')
        radio1.setChecked(True)
        vbox = QGridLayout()
        vbox.addWidget(radio1,0,0)
        vbox.addWidget(radio2,0,1)
        vbox.addWidget(radio3,0,2)
        box.setLayout(vbox)
        return box




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CollectScores()
    sys.exit(app.exec_())