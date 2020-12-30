
## free version
## Say Hello
# 추가

import sys

from PyQt5.QtWidgets import *

from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("main_windows.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setUI()

        self.textEdit.setText("안녕하세요")
        print(self.textEdit.toPlainText())


    def setUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.label.setText(self.textEdit.toPlainText())

if __name__ == "__main__":
    print("Hello World")
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    app.exec_()

