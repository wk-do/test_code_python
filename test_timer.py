import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import threading

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        # self.timer.timeout.connect(self.timeout)
        self.timer.timeout.connect(self.timer_slot)


    def timeout(self):
         now = datetime.datetime.now()
         self.statusBar().showMessage(str(now))


    def timer_slot(self):
        name = threading.currentThread().getName()
        print(f"timer slot is called by {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()