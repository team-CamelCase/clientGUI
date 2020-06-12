import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from subwindow import subWindow

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addStretch(1)

        label = QLabel("라즈베리파이 IP를 입력해주세요")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(25)
        label.setFont(font)
        self.label = label

        edit = QLineEdit()
        font = edit.font()
        font.setPointSize(20)
        edit.setFont(font)
        edit.setAlignment(Qt.AlignCenter)
        self.edit = edit

        button = QPushButton("시작하기")
        button.clicked.connect(self.onButtonClicked)
        button.setStyleSheet("background-color: #2ca8ff; color: #FFFFFF")
        button.resize(100, 50)
        self.button = button

        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addStretch(1)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def onButtonClicked(self):
        subwin = subWindow(self.edit.text())
        r = subwin.showSubWindow()

        if r:
            print("ok")
        else:
            print("-1")

    #def show(self):
        #super().show()
