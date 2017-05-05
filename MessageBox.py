import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.Yes |
                                     QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
