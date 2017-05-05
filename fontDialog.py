#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/5/5 21:56
@Author  : Zeroxus
@Site    : 
@File    : fontDialog.py
@Software: PyCharm
'''

import sys

from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,\
    QSizePolicy,QLabel,QFontDialog,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(20,20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)


        self.lbl = QLabel('Knowledge only matters',self)
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):
        #弹出一个字体选择对话框。getFont()方法返回一个字体名称和状态信息。状态信息有OK和其他两种。
        font,ok = QFontDialog.getFont()
        #点击OK，标签的字体就会随之更改
        if ok:
            self.lbl.setFont(font)


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())