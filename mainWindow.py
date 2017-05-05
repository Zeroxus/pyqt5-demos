import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #创建了一个文本编辑区域，并把它放在QMainWindow的中间区域。这个组件或占满所有剩余的区域
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('dog.png'),'Exit',self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&file')
        fileMenu.addAction(exitAction)

        toolBar = self.addToolBar('Exit')
        toolBar.addAction(exitAction)


        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Main Window')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())