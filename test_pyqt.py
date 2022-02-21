
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.q_hbox_layout()

        # label
    def label_buttone_signal_slot(self):
        self.label = QLabel("메시지: ", self)
        self.label.move(10, 10)

        # button
        self.btn = QPushButton("click", self)
        self.btn.move(10, 40)

        # signal-slot
        self.btn.clicked.connect(self.btn_clicked)

        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(10, 90)

        # StatusBar
    def status_bar(self):
        self.statusbar = QStatusBar(self)          # QStatusBar 객체 생성
        self.setStatusBar(self.statusbar)          # 위젯 배치


    def q_table_widget(self):
        # QTableWidget
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

    def q_hbox_layout(self):
        self.setGeometry(300, 300, 400, 300)

        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")
        btn3 = QPushButton("Button3")

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        self.setLayout(layout)


    def btn_clicked(self):
        self.label.clear()                  # 지우기
        self.label.setText("버튼 클릭")     # 텍스트 출력


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()