#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/5/6 15:02
@Author  : Zeroxus
@Site    : 
@File    : checkBox.py
@Software: PyCharm
'''

import sys

from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cb = QCheckBox('show title',self)#QCheckBox的构造器
        cb.move(20,20)
        cb.toggle()#设置窗口标题，我们就要检查单选框的状态。默认情况下，窗口没有标题，单选框未选中。
        #把changeTitle()方法和stateChanged信号关联起来。这样，changeTitle()就能切换窗口标题了
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheck Box')
        self.show()
    #控件的状态是由changeTitle()方法控制的，如果空间被选中，我们就给窗口添加一个标题，如果没被选中，就清空标题。
    def changeTitle(self,state):
        if state==Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())