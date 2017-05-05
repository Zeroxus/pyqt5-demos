import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event Handler')
        self.show()

        
    #我们重构了事件处理器函数keyPressEvent()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.key_Escape:
            self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())