# => This is the main file with all the UI and functions.

from sys import argv, exit
from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QFormLayout, QComboBox, QPushButton, QLineEdit, QMessageBox, \
    QApplication, QMainWindow, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QPoint
from PyQt5.QtGui import QFont, QIcon, QIntValidator, QDrag
from pandas import DataFrame
import Area
import Volume
import Functions
from title_bar import MyBar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        lightBlack = "#2B2B2B"
        fontColor  = "#A5BABA"
        black = "#3C3F41"
        
        # => Basic configurations & the title bar
        self.setAutoFillBackground(True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMinimumSize(560, 600)
        self.setStyleSheet("QMainWindow {background-color:"+lightBlack+"; border: 1px solid "+fontColor+"; border-radius: 8px;}")
        self.onlyInt = QIntValidator()

        self.title_frame = QFrame(self)
        self.title_frame.setGeometry(0, 0, 560, 50)
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(MyBar(self))
        self.title_frame.setLayout(self.layout1)
        self.layout1.setContentsMargins(0,0,0,0)
        self.layout1.addStretch(-1)


        # => Heading 
        self.headingLabel = QLabel(self)
        self.headingLabel.setText(" Area & Volume Calculator")
        self.headingLabel.setFont(QFont("Trebuchet MS", 20))
        self.headingLabel.setGeometry(70, 45, 400, 50)
        self.headingLabel.setStyleSheet(
            "color : "+fontColor+";text-decoration: underline;")

        self.frame_1 = QFrame(self)
        self.fl = QFormLayout(self)

        # => Selecting quantity and shape
        self.quantityLabel = QLabel(self)
        self.quantityLabel.setText("Quantity to be calculated : ")
        self.quantityLabel.setStyleSheet('color:'+fontColor+'')
        self.quantityLabel.setFont(QFont("Sogoe UI", 15))

        self.quantityCombo = QComboBox(self)
        self.quantityCombo.addItems(['Area', 'Surface Area', 'Volume'])
        self.quantityCombo.setFont(QFont('Sogoe UI', 15))
        self.quantityCombo.setFocusPolicy(Qt.NoFocus)
        self.quantityCombo.setFixedSize(200, 40)
        self.quantityCombo.setStyleSheet("QComboBox {background-color:"+black+"; color:"+fontColor+";}"
                                         "QComboBox:hover {background-color:"+lightBlack+"; color:"+fontColor+";}"
                                         "QComboBox QAbstractItemView {selection-background-color: "+lightBlack+";"
                                         "selection-color: "+fontColor+"; background-color: "+black+"; color: "+fontColor+"}")
        self.quantityCombo.currentTextChanged.connect(
            lambda: comboChange(self.quantityCombo.currentText()))

        self.shapeLabel = QLabel(self)
        self.shapeLabel.setText("Shape of the figure         : ")
        self.shapeLabel.setStyleSheet('color:'+fontColor+'')
        self.shapeLabel.setFont(QFont("Sogoe UI", 15))

        self.shapeCombo = QComboBox(self)
        self.shapeCombo.addItems(Area.shapes)
        self.shapeCombo.setFont(QFont('Sogoe UI', 15))
        self.shapeCombo.setFocusPolicy(Qt.NoFocus)
        self.shapeCombo.setFixedSize(200, 40)
        self.shapeCombo.setStyleSheet("QComboBox {background-color:"+black+"; color:"+fontColor+";}"
                                      "QComboBox:hover {background-color:"+lightBlack+"; color:"+fontColor+";}"
                                      "QComboBox QAbstractItemView {selection-background-color: "+lightBlack+";"
                                      "selection-color: "+fontColor+"; background-color: "+black+"; color: "+fontColor+"}")

        self.fl.addRow(self.quantityLabel, self.quantityCombo)
        self.fl.addRow(self.shapeLabel, self.shapeCombo)
        self.frame_1.setLayout(self.fl)
        self.frame_1.setGeometry(QRect(15, 110, 530, 120))

        # => Continue Button for showing the input fields
        self.continueButton = QPushButton(self)
        self.continueButton.setText("Continue")
        self.continueButton.setFont(QFont("Trebuchet MS", 15))
        self.continueButton.setStyleSheet('QPushButton {background-color:'+black+'; color:'+fontColor+'; border:2px outset black; border-radius: 8px}'
                                          'QPushButton:hover {background-color:'+lightBlack+'; color:'+fontColor+'; border:2px outset black;}'
                                          'QPushButton:pressed {background-color:'+black+'; color:'+fontColor+'; border:2px outset black;}')
        self.continueButton.clicked.connect(lambda: continueFunction(self.quantityCombo.currentText(),
                                                                     self.shapeCombo.currentText()))
        self.continueButton.setGeometry(30, 230, 500, 50)

        # => Frame with the value input fields
        self.input_frame = QFrame(self)
        self.input_frame.setStyleSheet('QFrame {background-color:'+black+'; color:'+fontColor+'; border:2px outset black; border-radius: 10px}')
        self.input_frame.setGeometry(QRect(30, 300, 500, 200))

        self.fl2 = QFormLayout(self.input_frame)
        self.input_frame.setLayout(self.fl2)

        # => Calculate Button
        self.calcButton = QPushButton(self.input_frame)
        self.calcButton.setText("Calculate")
        self.calcButton.setStyleSheet('QPushButton {background-color:'+lightBlack+'; color:'+fontColor+'; border:2px outset black; border-radius:5px}'
                                      'QPushButton:hover {background-color:'+black+'; color:'+fontColor+'; border:2px outset black;}'
                                      'QPushButton:pressed {background-color:'+lightBlack+'; color:'+fontColor+'; border:2px outset black;}')
        self.calcButton.setFont(QFont("Trebuchet MS", 15))
        self.calcButton.setGeometry(QRect(10, 147, 120, 40))
        self.calcButton.clicked.connect(lambda: calcFunc())
        self.calcButton.setHidden(True)

        self.resultField = QLineEdit(self.input_frame)
        self.resultField.setFont(QFont("Trebuchet MS", 15))
        self.resultField.setStyleSheet('QLineEdit {background-color:'+lightBlack+'; color:'+fontColor+'; border:2px outset black; border-radius:5px;    }')
        self.resultField.setText("Result : ")
        self.resultField.setReadOnly(True)
        self.resultField.setGeometry(QRect(140, 147, 350, 40))
        self.resultField.setHidden(True)
        self.resultField.setObjectName("resultField")
        
        # => Quit button
        self.quitButton = QPushButton(self)
        self.quitButton.setText("Quit")
        self.quitButton.setStyleSheet('QPushButton {background-color:'+black+'; color:'+fontColor+'; border:2px outset black; border-radius:8px;}'
                                      'QPushButton:hover {background-color:'+lightBlack+'; color:'+fontColor+'; border:2px outset black}'
                                      'QPushButton:pressed {background-color:'+black+'; color:'+fontColor+'; border:2px outset black;}')
        self.quitButton.setFont(QFont("Trebuchet MS", 15))
        self.quitButton.setGeometry(215, 520, 100, 50)
        self.quitButton.clicked.connect(QCoreApplication.instance().quit)
        
        self.link = QLabel(self)
        self.gitLink = "<a href = \"https://github.com/DevTushit17/A-V-S-C\" style = \"color: #A5BABA;\">Source Code</a>"
        self.link.setText(self.gitLink)
        self.link.setOpenExternalLinks(True)
        self.link.setFont(QFont("Trebutchet MS", 10))
        self.link.setGeometry(15, 560, 150, 40)
        
        self.creditButton = QPushButton(self)
        self.creditButton.setText("Credits")
        self.creditButton.setStyleSheet("QPushButton {color: "+fontColor+"; text-decoration: underline; border: 0px solid black; background-color: "+lightBlack+"}")
        self.creditButton.setFont(QFont("Trebutchet MS", 10))
        self.creditButton.setGeometry(487, 570, 60, 20)
        self.creditButton.clicked.connect(lambda: openCredits())
        
        self.pressing = False
        
        # => This function changes the values  in shapeCombo when value in quantityCombo is changed.
        def comboChange(quantity):
            dict1 = {'Area': Area.shapes.keys(),
                     'Surface Area': Volume.shapes.keys(),
                     'Volume': Volume.shapes.keys()}
            self.shapeCombo.clear()
            self.shapeCombo.addItems(dict1[quantity])


        def continueFunction(quantity, shape):
            self.calcButton.setHidden(False)
            self.resultField.setHidden(False)

            self.label1 = QLabel(self.input_frame)
            self.label2 = QLabel(self.input_frame)
            self.label3 = QLabel(self.input_frame)

            self.labelDict = {0: self.label1,
                              1: self.label2,
                              2: self.label3}

            self.field1 = QLineEdit(self.input_frame)
            self.field1.setValidator(self.onlyInt)
            self.field2 = QLineEdit(self.input_frame)
            self.field2.setValidator(self.onlyInt)
            self.field3 = QLineEdit(self.input_frame)
            self.field3.setValidator(self.onlyInt)

            self.lineEditDict = {0: self.field1,
                                 1: self.field2,
                                 2: self.field3}

            if self.fl2.rowCount() >= 0:
                for j in range(0, self.fl2.rowCount() + 1):
                    self.fl2.removeRow(0)

            num = 0
            if quantity == 'Area':
                num = len(Area.shapes[shape])
                for f in range(0, num):
                    self.labelDict[f].setText(Area.shapes[shape][f])
            elif quantity == 'Volume':
                num = len(Volume.shapes[shape])
                for f in range(0, num):
                    self.labelDict[f].setText(Volume.shapes[shape][f])
            elif quantity == 'Surface Area':
                num = len(Volume.shapes[shape])
                for f in range(0, num):
                    self.labelDict[f].setText(Volume.shapes[shape][f])

            for f in range(0, num):
                self.labelDict[f].setStyleSheet("QLabel {border:0px; color:"+fontColor+";}")
                self.labelDict[f].setFont(QFont("Trebuchet MS", 14))
                self.lineEditDict[f].setFont(QFont("Trebuchet MS", 14))
                self.lineEditDict[f].setStyleSheet("QLineEdit {background-color:"+lightBlack+"; color:"+fontColor+"; border:2px outset black; border-radius:5px;}"
                                                   "QLineEdit:hover {background-color:"+black+"; color:"+fontColor+"; border:2px outset black;}")
                self.fl2.addRow(self.labelDict[f], self.lineEditDict[f])

        def calcFunc():
            values = list()
            quantity = self.quantityCombo.currentText()
            shape = self.shapeCombo.currentText()
            fields = self.input_frame.findChildren(QLineEdit)
            for x in fields:
                if x.objectName() == 'resultField':
                    pass
                else:
                    values.append(x.text())
            values = DataFrame(values)
            values = values[values[0] != ""]
            values = values[0].tolist()
            values = [int(s) for s in values]
            for i in values:
                if i < 0:
                    self.errorBox_1 = QMessageBox(self)
                    self.errorBox_1.setText(
                        "One or more values is a negative integer.")
                    self.errorBox_1.setWindowTitle("Error")
                    self.errorBox_1.setIcon(QMessageBox.Critical)
                    self.errorBox_1.setStandardButtons(QMessageBox.Ok)
                    self.errorBox_1.show()
                    break
                else:
                    self.resultField.setText(
                        "Result : " + str(Functions.Connect(quantity, shape, values)))
                    
        def openCredits():
            self.creditBox = QMessageBox(self)
            self.creditBox.setWindowTitle("Credits")
            self.creditBox.setWindowIcon(QIcon("Icon.ico"))
            self.creditBox.setText("Python is used as the prgramming language. The following pakages are used: \n 1. PyQt5 \n 2. Pandas ")
            self.creditBox.setFont(QFont("Trebutchet MS", 12))
            self.creditBox.setStyleSheet("QMessageBox {background-color: "+lightBlack+";}"
                                         "QMessageBox QLabel {color: "+fontColor+";}"
                                         "QMessageBox QPushButton {color: "+fontColor+"; background-color: "+black+" }"
                                         "QMessageBox QPushButton:hover {color: "+fontColor+"; background-color: "+lightBlack+"}"
                                         "QMessageBox QPushButton:pressed    {color: "+fontColor+"; background-color: "+black+" }")
            self.creditBox.show()
            pass
                    
if __name__ == '__main__':
    app = QApplication(argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
