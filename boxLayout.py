import sys

from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout,QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")#创建了两个按钮
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()#创建一个水平布局
        hbox.addStretch(1)#stretch函数在两个按钮前面增加了一些弹性空间
        hbox.addWidget(okButton)#增加两个按钮和弹性空间
        hbox.addWidget(cancelButton)


        #我们把这个水平布局放到了一个垂直布局盒里面。弹性元素会把所有的元素一起都放置在应用的右下角。
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())