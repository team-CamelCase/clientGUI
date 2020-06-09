import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class manualMessage(QDialog):    
    def __init__(self, manualMsg, textIP):
        super().__init__()
        self.manualMsg = manualMsg
        self.textIP = textIP
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Manual Message Transmission')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addStretch(1)

        notice = QLabel()
        notice.setAlignment(Qt.AlignCenter)
        font = notice.font()
        font.setPointSize(20)
        notice.setFont(font)
        notice.setText("Changing text message into voice file...")
        self.notice = notice

        getVoiceFile = QProcess(self)
        getVoiceFile.finished.connect(self.getVoiceFileFinished)
        getVoiceFile.start('python', ['test.py'])

        backButton = QPushButton("Go Back")
        backButton.clicked.connect(self.backButtonClicked)

        layout.addWidget(self.notice)
        layout.addWidget(backButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def getVoiceFileFinished(self, exitCode, exitStatus):
        if exitCode == 0: #success
            self.notice.setText("Sending file...")

            sendFile = QProcess(self)
            sendFile.finished.connect(self.sendFileFinished)
            sendFile.start('python', ['test.py'])
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def sendFileFinished(self, exitCode, exitStatus):
        if exitCode == 0:
            self.notice.setText("Done!")
        else:
            self.notice.setText("Something wrong.. Try again!")

    def backButtonClicked(self):
        self.accept()
        
    def showManualMsgWindow(self):
        return super().exec_()

