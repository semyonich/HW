from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QDateEdit, \
     QRadioButton, QCheckBox, QLabel, QPlainTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_interface()

    def init_interface(self):
        f_name = QLineEdit(self)
        f_name.setPlaceholderText("First name:")
        f_name.setObjectName("f_name")
        f_name.move(100, 20)
        f_name.resize(100, 20)

        l_name = QLineEdit(self)
        l_name.setPlaceholderText("Last name:")
        l_name.setObjectName("l_name")
        l_name.move(100, 50)
        l_name.resize(100, 20)

        email = QLineEdit(self)
        email.setPlaceholderText("Email:")
        email.setObjectName("email")
        email.move(100, 80)
        email.resize(100, 20)

        bio = QPlainTextEdit(self)
        bio.setPlaceholderText("Bio:")
        bio.setObjectName("bio")
        bio.move(250, 20)
        bio.resize(200, 50)

        date = QDateEdit(self)
        date.setObjectName("date")
        date.move(100, 110)
        date.resize(100, 20)

        self.setGeometry(200, 200, 500, 400)  # left top width height
        self.setWindowTitle("Registration form.")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())