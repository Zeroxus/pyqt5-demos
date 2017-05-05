"""
这个示例有一个按钮和一个输入框，点击按钮显示对话框，输入的文本会显示在输入框里。
"""


import sys

from PyQt5.QtWidgets import QApplication,QWidget,\
    QPushButton,QInputDialog,QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showDialog(self):
        #显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符。
        # 对话框返回输入内容和一个布尔值，如果点击的是OK按钮，布尔值就返回True
        text,ok = QInputDialog.getText(self,'Input Dialog',
                                       'Enter your name')
        if ok:
            self.le.setText(str(text))

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())