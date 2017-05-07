#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/5/7 22:16
@Author  : Zeroxus
@Site    : 
@File    : slider.py
@Software: PyCharm
'''

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QSlider,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal,self)#创建一个水平的QSlider
        sld.setGeometry(30,40,100,30)
        #把valueChanged信号跟changeValue()方法关联起来。
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('speaker.png'))
        self.label.setGeometry(160,40,80,30)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider')
        self.show()

    #根据音量值的大小更换标签位置的图片
    def changeValue(self,value):
        if value ==0:
            self.label.setPixmap(QPixmap('speaker.png'))
        elif value>0 and value<=30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value>30 and value<80:
            self.label.setPixmap(QPixmap('max.png'))
        else:
            self.label.setPixmap(QPixmap('speaker.png'))


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())