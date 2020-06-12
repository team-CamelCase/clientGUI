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
        notice.setText("음성 파일로 변환 중입니다...")
        self.notice = notice

        makeVoiceFile = QProcess(self)
        makeVoiceFile.finished.connect(self.makeVoiceFileFinished)
        makeVoiceFile.start('python', ['makeVoiceFile.py', '--text', self.manualMsg])
        self.makeVoiceFile = makeVoiceFile

        backButton = QPushButton("뒤로 가기")
        backButton.clicked.connect(self.backButtonClicked)
        
        layout.addWidget(self.notice)
        layout.addWidget(backButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def makeVoiceFileFinished(self, exitCode, exitStatus):
        output = str(self.makeVoiceFile.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        status = output.split("\\r\\n")[0]
        print(status)

        if status == '200': #success
            self.notice.setText("파일 경로를 얻어오고 있습니다...")

            getFile = QProcess(self)
            getFile.finished.connect(self.getFileFinished)
            getFile.start('python', ['test.py'])
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def getFileFinished(self, exitCode, exitStatus):
        print(exitCode)
        if exitCode == 0: #success
            self.notice.setText("파일을 전송하고 있습니다...")

            sendFile = QProcess(self)
            sendFile.finished.connect(self.sendFileFinished)
            sendFile.start('python', ['test.py'])
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def sendFileFinished(self, exitCode, exitStatus):
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
            self.notice.setText("수동 전송 완료!")
        else:
            self.notice.setText("Something wrong.. Try again!")

    def backButtonClicked(self):
        self.accept()
        
    def showManualMsgWindow(self):
        return super().exec_()

