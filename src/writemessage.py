import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from manualmessage import manualMessage

class writeMessage(QDialog):    
    def __init__(self, textIP, frequency):
        super().__init__()
        self.textIP = textIP
        self.frequency = frequency
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Manual Message Transmission')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addStretch(1)

        #title of message
        title = QLabel("제목:")
        title.setAlignment(Qt.AlignCenter)
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        self.title = title

        titleEdit = QLineEdit()
        font = titleEdit.font()
        font.setPointSize(20)
        titleEdit.setFont(font)
        self.titleEdit = titleEdit

        #body of message
        content = QLabel("메시지를 입력하세요:")
        content.setAlignment(Qt.AlignCenter)
        font = content.font()
        font.setPointSize(20)
        content.setFont(font)
        self.content = content

        contentEdit = QLineEdit()
        font = contentEdit.font()
        font.setPointSize(20)
        contentEdit.setFont(font)
        self.contentEdit = contentEdit

        completeButton = QPushButton("전송 하기")
        completeButton.clicked.connect(self.completeButtonClicked)
        
        layout.addWidget(self.title)
        layout.addWidget(self.titleEdit)
        layout.addWidget(self.content)
        layout.addWidget(self.contentEdit)
        layout.addWidget(completeButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()

    def completeButtonClicked(self):
        manualmsg = manualMessage(self.titleEdit.text(),
                                  self.contentEdit.text(),
                                  self.textIP,
                                  self.frequency)
        r = manualmsg.showManualMsgWindow()

        if r is not None:
            print("Manual Sending SUCCESS")
            self.accept()
        
    def showWriteWindow(self):
        return super().exec_()
