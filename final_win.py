from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QApplication, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.line = QVBoxLayout()
        self.txt_index = QLabel(txt_index)
        self.txt_heartwork = QLabel(txt_heartwork)