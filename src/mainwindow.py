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

        label = QLabel("RasberryPie IP:")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        self.label = label

        edit = QLineEdit()
        font = edit.font()
        font.setPointSize(20)
        edit.setFont(font)
        self.edit = edit

        button = QPushButton("Start watchOut!")
        button.clicked.connect(self.onButtonClicked)
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
