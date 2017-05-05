#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/5/5 22:28
@Author  : Zeroxus
@Site    : 
@File    : fileDialog.py
@Software: PyCharm
'''

import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QAction,QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    #设置了一个文本编辑框，文本编辑框是基于QMainWindow组件的。
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('dog.png'),'Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        #弹出QFileDialog窗口。getOpenFileName()方法的第一个参数是说明文字，
        # 第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件
        fname = QFileDialog.getOpenFileName(self,'Open File', '/home')
        #读取选中的文件，并显示在文本编辑框内
        if fname[0]:
            f = open(fname[0],'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())