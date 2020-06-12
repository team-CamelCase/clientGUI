import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class autoMessage(QDialog):    
    def __init__(self, numMsg, textIP, infoList):
        super().__init__()
        self.numMsg = numMsg
        self.textIP = textIP
        self.infoList = infoList
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Auto Message Transmission')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addStretch(1)

        notice = QLabel()
        notice.setAlignment(Qt.AlignCenter)
        font = notice.font()
        font.setPointSize(20)
        notice.setFont(font)
        notice.setText("파일 경로를 얻어오고 있습니다...")
        self.notice = notice

        getFiles = QProcess(self)
        getFiles.finished.connect(self.getFilesFinished)
        getFiles.start('python', ['test.py'])
        
        backButton = QPushButton("뒤로 가기")
        backButton.clicked.connect(self.backButtonClicked)

        layout.addWidget(self.notice)
        layout.addWidget(backButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def getFilesFinished(self, exitCode, exitStatus):
        print(exitCode)
        if exitCode == 0: #success
            self.notice.setText("파일을 전송하고 있습니다...")

            sendFiles = QProcess(self)
            sendFiles.finished.connect(self.sendFilesFinished)
            sendFiles.start('python', ['test.py'])
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def sendFilesFinished(self, exitCode, exitStatus):
        print(exitCode)
        if exitCode == 0:
            self.notice.setText("라디오에 송출 중입니다...")

            executeRadio = QProcess(self)
            executeRadio.finished.connect(self.executeRadioFinished)
            executeRadio.start('python', ['test.py'])
        else:
            self.notice.setText("Something wrong.. Try again!")

    def executeRadioFinished(self, exitCode, exitStatus):
        print(exitCode)
        if exitCode == 0:
            self.notice.setText("자동 전송 완료!")
        else:
            self.notice.setText("Something wrong.. Try again!")

    def backButtonClicked(self):
        self.accept()
        
    def showAutoMsgWindow(self):
        return super().exec_()
