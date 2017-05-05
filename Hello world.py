import sys
from PyQt5.QtWidgets import QApplication,QWidget#引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件。

if __name__=="__main__":
    #每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。
    # Python可以在shell里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)

    #QWidget空间是一个用户界面的基本空间，它提供了基本的应用构造器。
    #默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。
    w = QWidget()
    w.resize(250,150)#改变控件的大小,宽250px，高150px
    w.move(300,300)#修改控件位置,把控件放置到屏幕坐标的(300, 300)的位置。注：屏幕坐标系的原点是屏幕的左上角。
    w.setWindowTitle('simple')#添加了一个标题，标题在标题栏展示
    w.show()#控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来
    sys.exit(app.exec_())#进入了应用的主循环中，事件处理器这个时候开始工作，sys.exit()方法能确保主循环安全退出