import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class manualMessage(QDialog):    
    def __init__(self, manualMsgTitle, manualMsgContent, textIP, frequency):
        super().__init__()
        self.manualMsgTitle = manualMsgTitle
        self.manualMsgContent = manualMsgContent
        self.textIP = textIP
        self.frequency = frequency
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
        notice.setText("음성 파일 경로를 받아오는 중입니다...")
        self.notice = notice

        getVoiceFile = QProcess(self)
        getVoiceFile.finished.connect(self.getVoiceFileFinished)
        getVoiceFile.start('python', ['getVoiceFile.py',
                                      '--title', self.manualMsgTitle,
                                      '--content', self.manualMsgContent])
        self.getVoiceFile = getVoiceFile

        backButton = QPushButton("뒤로 가기")
        backButton.clicked.connect(self.backButtonClicked)
        
        layout.addWidget(self.notice)
        layout.addWidget(backButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def getVoiceFileFinished(self, exitCode, exitStatus):
        output = str(self.getVoiceFile.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        output = list(output.split("\\r\\n"))
        status = output[0]
        self.voiceFilePath = output[1]
        print(status, self.voiceFilePath)

        if status == '200': #success
            self.notice.setText("저장소 토큰을 얻어오고 있습니다...")

            getToken = QProcess(self)
            getToken.finished.connect(self.getTokenFinished)
            getToken.start('python', ['getToken.py'])
            self.getToken = getToken
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def getTokenFinished(self, exitCode, exitStatus):
        output = str(self.getToken.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        output = list(output.split("\\r\\n"))
        status = output[0]
        self.token = output[1]
        print(status, self.token)
        
        if status == '200': #success
            self.notice.setText("파일을 전송하고 있습니다...")

            sendFile = QProcess(self)
            sendFile.finished.connect(self.sendFileFinished)
            sendFile.start('python', ['sendFile.py',
                                      '--ip', self.textIP,
                                      '--path', self.voiceFilePath,
                                      '--token', self.token,
                                      '--numMsg', str(1)])
            self.sendFile = sendFile
        else: #fail
            self.notice.setText("Something wrong.. Try again!")

    def sendFileFinished(self, exitCode, exitStatus):
        output = str(self.getToken.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        output = list(output.split("\\r\\n"))
        status = output[0]
        print(status)
        
        if status == '200':
            self.notice.setText("라디오에 송출 중입니다...")

            executeRadio = QProcess(self)
            executeRadio.finished.connect(self.executeRadioFinished)
            executeRadio.start('python', ['executeRadio.py',
                                          '--ip', self.textIP,
                                          '--filename', self.manualMsgTitle,
                                          '--frequency', self.frequency])
            self.executeRadio = executeRadio
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
