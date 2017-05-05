import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #创建一个QGridLayout实例，并把它放到程序窗口里
        grid = QGridLayout()
        self.setLayout(grid)

        #我们将要使用的按钮的名称
        names = ['Cls','Bck','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        #创建按钮位置列表
        positions = [(i,j) for i in range(5) for j in range(4)]

        #创建按钮，并使用addWidget()方法把按钮放到布局里面
        for position,name in zip(positions,names):
            if name=='':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())