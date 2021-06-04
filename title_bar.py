from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QStyle, QGridLayout, QFrame
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QSize

class MyBar(QWidget):
    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        self.layout = QGridLayout()
        
        self.icon = QPixmap("Icon.ico")
        self.iconLabel = QLabel(self)
        # self.iconLabel.setStyleSheet("background-color: pink")
        self.iconLabel.setMaximumWidth(35)
        self.iconLabel.setPixmap(self.icon)
        
        self.title = QLabel(self)
        self.title.setText("A-V-S-C")
        self.title.setWindowIcon(QIcon("Icon.ico"))
        self.title.setFont(QFont("Trebutchet MS", 12))
        self.title.setStyleSheet("color : #A5BABA; ")
        
        self.btn_close = QPushButton(self)
        self.btn_close.setIcon(QIcon("close.png"))
        self.btn_close.setMaximumWidth(30)
        self.btn_close.setMinimumHeight(30)
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setStyleSheet("QPushButton {background-color: #2B2B2B; border: 0px solid black;}"
                                     "QPushButton:hover {background-color: #bc2020; border: 0px solid black}"
                                     "QPushButton:pressed {background-color: #771515; border: 0px solid black;}")

        self.btn_min = QPushButton(self)
        self.btn_min.setIcon(QIcon("minimise.png"))
        self.btn_min.setMaximumWidth(30)
        self.btn_min.setMinimumHeight(30)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setStyleSheet("QPushButton {background-color: #2B2B2B; border: 0px solid black;}"
                                   "QPushButton:hover {background-color: #3C3F41; border: 0px solid black}"
                                   "QPushButton:pressed {background-color: #2B2B2B; border: 0px solid black;}")
        
        self.layout.addWidget(self.iconLabel, 0, 0)
        self.layout.addWidget(self.title, 0, 1)
        self.layout.addWidget(self.btn_min, 0, 2)
        self.layout.addWidget(self.btn_close, 0, 3)
        self.setLayout(self.layout)
        
        self.start = QPoint(0, 0)
        self.pressing = False

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_min_clicked(self):
        self.parent.showMinimized()