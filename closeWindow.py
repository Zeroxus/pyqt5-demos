import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon,QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #创建一个继承自QPushButton的按钮。第一个参数是按钮的文本，
        # 第二个参数是按钮的父级组件，这个例子中，父级组件就是我们创建的继承自Qwidget的Example类。
        qbtn = QPushButton('Quit',self)
        #QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例。
        # QCoreApplication是在QApplication里创建的。 点击事件和能终止进程并退出应用的quit函数绑定在了一起
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowIcon(QIcon('dog.png'))
        self.setWindowTitle('Quit Button')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())