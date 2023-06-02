from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QApplication, QVBoxLayout
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.next_click()
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
    def connects(self):
        self.btn_next.clicked.connect(self.next_clicked)
    def show(self):
        self.show()
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
