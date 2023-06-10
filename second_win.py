from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QGroupBox, QRadioButton, QListWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
      
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.txt_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_timer = QLabel(txt_timer)

        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_hintage = QLineEdit(txt_hintage)
        self.txt_starttest1 = QLineEdit(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_starttest2 = QLineEdit(txt_starttest2)
        self.txt_starttest3 = QLineEdit(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)

        self.l_line.addWidget(self.txt_name, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_hintname, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_age, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_hintage, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_test1, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_starttest1, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_hinttest1, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_test2, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_starttest2, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_test3, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_starttest3, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_hinttest2, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_hinttest3, Qt.AlignCenter)
        self.l_line.addWidget(self.txt_sendresults, Qt.AlignCenter)
        self.r_line.addWidget(self.txt_timer, Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.txt_sendresults.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)


    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    

    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFront(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.txt_timer.setStyleSheet('collor: rgb(0,0,0)')
        self.txt_timer.setFont(QFont('Times',36,QFont.Bold))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    


    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.txt_timer.setStyleSheet("color: rgb(0, 255 ,0)")
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.txt_timer.setStyleSheet("color: rgb(0, 255 ,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.txt_timer.setFont(QFont('Times',36, QFont.Bold))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
