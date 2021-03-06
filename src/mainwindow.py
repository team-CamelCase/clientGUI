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

        #rasberry pi ip
        ip = QLabel("라즈베리파이 IP 주소:")
        ip.setAlignment(Qt.AlignCenter)
        font = ip.font()
        font.setPointSize(25)
        ip.setFont(font)
        self.ip = ip

        ipEdit = QLineEdit()
        font = ipEdit.font()
        font.setPointSize(20)
        ipEdit.setFont(font)
        self.ipEdit = ipEdit

        #frequency
        frequency = QLabel("주파수 설정:")
        frequency.setAlignment(Qt.AlignCenter)
        font = frequency.font()
        font.setPointSize(25)
        frequency.setFont(font)
        self.frequency = frequency

        freqEdit = QLineEdit()
        font = freqEdit.font()
        font.setPointSize(20)
        freqEdit.setFont(font)
        self.freqEdit = freqEdit

        button = QPushButton("시작하기")
        button.clicked.connect(self.onButtonClicked)
        button.setStyleSheet("background-color: #2ca8ff; color: #FFFFFF")
        button.resize(100, 50)
        self.button = button

        layout.addWidget(self.ip)
        layout.addWidget(self.ipEdit)
        layout.addWidget(self.frequency)
        layout.addWidget(self.freqEdit)
        layout.addWidget(self.button)
        layout.addStretch(1)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def onButtonClicked(self):
        subwin = subWindow(self.ipEdit.text(), self.freqEdit.text())
        r = subwin.showSubWindow()

        if r:
            print("ok")
        else:
            print("-1")

    #def show(self):
        #super().show()
