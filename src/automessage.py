import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class autoMessage(QDialog):    
    def __init__(self, numMsg, textIP, frequency, titleStr):
        super().__init__()
        self.numMsg = numMsg
        self.textIP = textIP
        self.frequency = frequency
        self.titleStr = titleStr
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
        notice.setText("파일 경로를 받아오고 있습니다...")
        self.notice = notice

        getFiles = QProcess(self)
        getFiles.finished.connect(self.getFilesFinished)
        getFiles.start('python', ['getFiles.py',
                                  '--numMsg', str(self.numMsg),
                                  '--titleStr', self.titleStr])
        self.getFiles = getFiles
        
        backButton = QPushButton("뒤로 가기")
        backButton.clicked.connect(self.backButtonClicked)

        layout.addWidget(self.notice)
        layout.addWidget(backButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def getFilesFinished(self, exitCode, exitStatus):
        output = str(self.getFiles.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        output = list(output.split("\\r\\n"))
        status = output[0]
        self.finalNumMsg = output[1]
        self.voiceFilePaths = output[2]
        #voiceFilePaths = voiceFilePaths[1:-1] #detach '[', ']'
        print(status, self.finalNumMsg, self.voiceFilePaths)

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

            sendFiles = QProcess(self)
            sendFiles.finished.connect(self.sendFilesFinished)
            sendFiles.start('python', ['sendFiles.py',
                                      '--ip', self.textIP,
                                      '--path', self.voiceFilePaths,
                                      '--token', self.token,
                                       '--numMsg', str(self.finalNumMsg)])
            self.sendFiles = sendFiles
        else: #fail
            self.notice.setText("Something wrong.. Try again!")


    def sendFilesFinished(self, exitCode, exitStatus):
        print(str(self.sendFiles.readAll()))
        print(exitCode)
        print("---******8-------")
        if exitCode == 0:
            self.notice.setText("라디오에 송출 중입니다...")

            executeRadio = QProcess(self)
            executeRadio.finished.connect(self.executeRadioFinished)
            executeRadio.start('python', ['executeRadios.py',
                                          '--ip', self.textIP,
                                          '--filename', self.voiceFilePaths,
                                          '--frequency', self.frequency])
            self.executeRadio = executeRadio
        else:
            self.notice.setText("Something wrong.. Try again!")

    def executeRadioFinished(self, exitCode, exitStatus):
        print(exitCode)
        print("&&&&&&&&&&&&&&&")
        print(str(self.executeRadio.readAll()))
        if exitCode == 0:
            self.notice.setText("자동 전송 완료!")
        else:
            self.notice.setText("Something wrong.. Try again!")

    def backButtonClicked(self):
        self.accept()
        
    def showAutoMsgWindow(self):
        return super().exec_()
