import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from automessage import autoMessage

class selectMessage(QDialog):    
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

        #make label name list for infos
        infoLabels = []
        for num in range(self.numMsg):
            infoLabel = "info" + str(num)
            infoLabels.append(infoLabel)

        #print(infoLabels)
            
        getInfos = QProcess(self)
        #getInfos.finished.connect(self.getInfosFinished)
        getInfos.start('python', ['getInfo.py'])
        getInfos.waitForFinished()
        self.getInfos = getInfos
        output = str(getInfos.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        infos = list(output.split("\\n"))

        print(infos)
        
        #set checkbox ui for each info labels
        self.infoCheckBoxes = []
        for idx, info in enumerate(infoLabels):
            info = QCheckBox(infos[idx], self)
            self.infoCheckBoxes.append(info)
            layout.addWidget(info)
            
        #print(self.infoCheckBoxes)

        completeButton = QPushButton("전송 하기")
        completeButton.clicked.connect(self.completeButtonClicked)
        
        #layout.addWidget(self.notice)
        layout.addWidget(completeButton)
        layout.addStretch(1)

        self.setLayout(layout)

        self.accept()


    def completeButtonClicked(self):
        infoToSend = []

        for infoCheckBox in self.infoCheckBoxes:
            if infoCheckBox.isChecked():
                infoToSend.append(infoCheckBox.text())

        print(infoToSend)
            
        automsg = autoMessage(self.numMsg, self.textIP, infoToSend)
        r = automsg.showAutoMsgWindow()

        if r is not None:
            print("Auto Sending SUCESS!")
            self.accept()
        
    def showSelectWindow(self):
        return super().exec_()
