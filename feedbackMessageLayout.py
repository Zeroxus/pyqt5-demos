import sys

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,\
    QLineEdit,QTextEdit,QGridLayout,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #创建了一个有三个标签的窗口。两个行编辑和一个文版编辑
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)#创建标签之间的空间

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)#可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5列显示。

        self.setLayout(grid)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Review')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())