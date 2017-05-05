import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #QAction是菜单栏、工具栏或者快捷键的动作的组合
        exitAction = QAction(QIcon('dog.png'),'&Exit',self)#创建了一个图标、一个exit的标签
        exitAction.setShortcut('ctrl+Q')#一个快捷键组合
        exitAction.setStatusTip('Exit Application')#创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态


        #执行这个指定的动作时，就触发了一个事件。
        # 这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()#创建了一个菜单栏
        fileMenu = menuBar.addMenu('&File')#在上面添加了一个file菜单
        fileMenu.addAction(exitAction)#关联了点击退出应用的事件

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Menu Bar')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())