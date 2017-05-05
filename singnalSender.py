import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSignal,QObject

class Comunication(QObject):
    closeApp = pyqtSignal()#创建了一个pyqtSignal()属性的信号

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Comunication()
        self.c.closeApp.connect(self.close)#closeApp信号QMainWindow的close()方法绑定

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit Signal')
        self.show()
    #重构mousePressEvent方法
    def mousePressEvent(self, event):
        self.c.closeApp.emit()#当点击窗口的时候，closeApp信号发送，程序终止

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())