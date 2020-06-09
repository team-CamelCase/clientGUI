import sys
from PyQt5.QtWidgets import *
from mainwindow import mainWindow
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())
