import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class autoMessage(QDialog):    
    def __init__(self, numMsg, textIP):
        super().__init__()
        self.numMsg = numMsg
        self.textIP = textIP
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
        myText = "Getting " + str(self.numMsg) + " files..."
        notice.setText(myText)
        self.notice = notice

        getFiles = QProcess(self)
        getFiles.finished.connect(self.getFilesFinished)
        getFiles.start('python', ['test.py'])

        backButton = QPushButton("Go Back")
        backButton.clicked.connect(self.backButtonClicked)

        layout.addWidget(self.notice)
        layout.addWidget(backButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def getFilesFinished(self, exitCode, exitStatus):
        if exitCode == 0: #success
            self.notice.setText("Sending files...")

            sendFiles = QProcess(self)
            sendFiles.finished.connect(self.sendFilesFinished)
            sendFiles.start('python', ['test.py'])
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def sendFilesFinished(self, exitCode, exitStatus):
        if exitCode == 0:
            self.notice.setText("Done!")
        else:
            self.notice.setText("Something wrong.. Try again!")

    def backButtonClicked(self):
        self.accept()
        
    def showAutoMsgWindow(self):
        return super().exec_()
