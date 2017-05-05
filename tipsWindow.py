import sys

from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont,QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))#使用了10px的SansSerif字体
        #调用setTooltip()创建提示框可以使用富文本格式的内容。
        self.setToolTip('This is a <b>QWidget</b> widget')
        #创建了一个按钮，并且为按钮添加了一个提示框。
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()方法提供了一个默认的按钮大小。
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Tool Tips')
        self.setWindowIcon(QIcon('dog.png'))
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())

