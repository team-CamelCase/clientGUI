import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from automessage import autoMessage

class selectMessage(QDialog):    
    def __init__(self, numMsg, textIP, frequency):
        super().__init__()
        self.numMsg = numMsg
        self.textIP = textIP
        self.frequency = frequency
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Auto Message Transmission')
        self.setGeometry(100, 100, 700, 400)
        
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
        getInfos.start('python', ['getInfoList.py',
                                  '--numMsg', str(self.numMsg)])
        getInfos.waitForFinished()
        output = str(getInfos.readAll())
        output = output[2:-1] #detach first "b'", last "'"
        output = list(output.split("\\r\\n"))
        status = output[0]
        titleList = output[1]
        titleList = titleList[1:-1] #detach '[', ']'
        titleList = list(titleList.split(', '))
        print(titleList, type(titleList))
        #self.getInfos = getInfos
        
        #set checkbox ui for each info labels
        self.infoCheckBoxes = []
        for idx, info in enumerate(titleList):
            info = QCheckBox(titleList[idx][1:-1], self)
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
        infoToSend = ""

        for infoCheckBox in self.infoCheckBoxes:
            if infoCheckBox.isChecked():
                infoToSend += infoCheckBox.text()
                infoToSend += ','

        infoToSend = infoToSend[:-1] #detach last ','
        print(infoToSend)
            
        automsg = autoMessage(self.numMsg, self.textIP,
                              self.frequency, infoToSend)
        r = automsg.showAutoMsgWindow()

        if r is not None:
            print("Auto Sending SUCESS!")
            self.accept()
        
    def showSelectWindow(self):
        return super().exec_()
