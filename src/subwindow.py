import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from automessage import autoMessage
from manualmessage import manualMessage

class subWindow(QDialog):    
    def __init__(self, textIP):
        super().__init__()
        self.textIP = textIP
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Sub Window')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addStretch(1)

        myIP = QLabel()
        myIP.setAlignment(Qt.AlignCenter)
        font = myIP.font()
        font.setPointSize(20)
        myIP.setFont(font)
        myIP.setText(self.textIP)
        
        autoButton = QPushButton("자동 전송")
        autoButton.clicked.connect(self.autoButtonClicked)

        manualButton = QPushButton("수동 전송")
        manualButton.clicked.connect(self.manualButtonClicked)
        
        subLayout = QHBoxLayout()
        subLayout.addWidget(autoButton)
        subLayout.addWidget(manualButton)

        layout.addWidget(myIP)
        layout.addLayout(subLayout)
        layout.addStretch(1)

        self.setLayout(layout)

    def autoButtonClicked(self):
        #self.accept()
        numMsg, OK = QInputDialog.getInt(self, "Auto Message Input",
                                         "Select number of messages to send")
        if OK:
            automsg = autoMessage(numMsg, self.textIP)
            r = automsg.showAutoMsgWindow()

        if r is not None:
            print("Auto Sending SUCCESS!")
            self.accept()
            
    def manualButtonClicked(self):
        #self.reject()
        manualMsg, OK = QInputDialog.getText(self, "Manual Message Input",
                                         "Write input message to send")

        if OK:
            manualmsg = manualMessage(manualMsg, self.textIP)
            r = manualmsg.showManualMsgWindow()

        if r is not None:
            print("Manual Sending SUCCESS!")
            self.accept()

    def showSubWindow(self):
        return super().exec_()
