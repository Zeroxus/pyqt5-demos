import sys

from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()#调用我们下面写的，实现对话框居中的方法

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()#得到了主窗口的大小。
        #QtGui.QDesktopWidget类提供了用户的桌面信息，其中就有屏幕的大小。
        cp = QDesktopWidget().availableGeometry().center()#获取到显示器的分辨率，然后得到了中间点的位置。
        qr.moveCenter(cp)#把自己窗口的中心点放置到qr的中心点。
        self.move(qr.topLeft())#把窗口的坐上角移动到qr的矩形的左上角上，这样就居中了我们自己的窗口

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())