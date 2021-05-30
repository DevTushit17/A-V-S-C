from sys import argv, exit
from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QFormLayout, QComboBox, QPushButton, QLineEdit, QMessageBox, QApplication
from PyQt5.QtCore import Qt, QRect, QCoreApplication
from PyQt5.QtGui import QFont, QIcon, QIntValidator
import Area
import Volume
import Functions
from pandas import DataFrame


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.onlyInt = QIntValidator()

        self.setWindowTitle("Area & Volume Calculator")
        self.setMinimumSize(560, 545)
        self.setMaximumSize(560, 545)
        self.setWindowIcon(QIcon("Icon.ico"))
        self.setStyleSheet("background-color:#2B2B2B;")

        self.frame_1 = QFrame(self)

        self.headingLabel = QLabel(self)
        self.headingLabel.setText(" Area & Volume Calculator")
        self.headingLabel.setFont(QFont("Trebuchet MS", 20))
        self.headingLabel.setGeometry(70, 15, 400, 50)
        self.headingLabel.setStyleSheet(
            "color : #A5BABA;text-decoration: underline;")

        self.fl = QFormLayout(self)

        self.quantityLabel = QLabel(self)
        self.quantityLabel.setText("Quantity to be calculated : ")
        self.quantityLabel.setStyleSheet('color:#A5BABA')
        self.quantityLabel.setFont(QFont("Sogoe UI", 15))

        self.quantityCombo = QComboBox(self)
        self.quantityCombo.addItems(['Area', 'Surface Area', 'Volume'])
        self.quantityCombo.setFont(QFont('Sogoe UI', 15))
        self.quantityCombo.setFocusPolicy(Qt.NoFocus)
        self.quantityCombo.setFixedSize(200, 40)
        self.quantityCombo.setStyleSheet(
            "background-color:#3C3F41; color:#A5BABA;")
        self.quantityCombo.currentTextChanged.connect(
            lambda: comboChange(self.quantityCombo.currentText()))

        self.shapeLabel = QLabel(self)
        self.shapeLabel.setText("Shape of the figure         : ")
        self.shapeLabel.setStyleSheet('color:#A5BABA')
        self.shapeLabel.setFont(QFont("Sogoe UI", 15))

        self.shapeCombo = QComboBox(self)
        self.shapeCombo.addItems(Area.shapes)
        self.shapeCombo.setFont(QFont('Sogoe UI', 15))
        self.shapeCombo.setFocusPolicy(Qt.NoFocus)
        self.shapeCombo.setFixedSize(200, 40)
        self.shapeCombo.setStyleSheet(
            "background-color:#3C3F41; color:#A5BABA;")

        self.fl.addRow(self.quantityLabel, self.quantityCombo)
        self.fl.addRow(self.shapeLabel, self.shapeCombo)
        self.frame_1.setLayout(self.fl)
        self.frame_1.setGeometry(QRect(15, 70, 530, 120))

        self.continueButton = QPushButton(self)
        self.continueButton.setText("Continue")
        self.continueButton.setFont(QFont("Trebuchet MS", 15))
        self.continueButton.setStyleSheet(
            'background-color:#3C3F41; color:#A5BABA; border:2px outset black;')
        self.continueButton.clicked.connect(lambda: continueFunction(self.quantityCombo.currentText(),
                                                                     self.shapeCombo.currentText()))
        self.continueButton.setGeometry(30, 190, 500, 50)

        self.frame_2 = QFrame(self)
        self.frame_2.setStyleSheet(
            'background-color:#3C3F41; color:#A5BABA; border:2px outset black;')
        self.frame_2.setGeometry(QRect(30, 260, 500, 200))

        self.fl2 = QFormLayout(self.frame_2)
        self.frame_2.setLayout(self.fl2)

        self.calcButton = QPushButton(self.frame_2)
        self.calcButton.setText("Calculate")
        self.calcButton.setStyleSheet(
            'background-color:#2B2B2B; color:#A5BABA; border:2px outset black;')
        self.calcButton.setFont(QFont("Trebuchet MS", 15))
        self.calcButton.setGeometry(QRect(10, 147, 120, 40))
        self.calcButton.clicked.connect(lambda: calcFunc())
        self.calcButton.setHidden(True)

        self.resultFrame = QLineEdit(self.frame_2)
        self.resultFrame.setFont(QFont("Trebuchet MS", 15))
        self.resultFrame.setStyleSheet(
            'background-color:#2B2B2B; color:#A5BABA; border:2px outset black;')
        self.resultFrame.setText("Result : ")
        self.resultFrame.setReadOnly(True)
        self.resultFrame.setGeometry(QRect(140, 147, 350, 40))
        self.resultFrame.setHidden(True)
        self.resultFrame.setObjectName("resultFrame")

        self.quitButton = QPushButton(self)
        self.quitButton.setText("Quit")
        self.quitButton.setStyleSheet(
            'background-color:#3C3F41; color:#A5BABA; border:2px outset black;')
        self.quitButton.setFont(QFont("Trebuchet MS", 15))
        self.quitButton.setGeometry(215, 480, 100, 50)
        self.quitButton.clicked.connect(QCoreApplication.instance().quit)

        self.show()

        def comboChange(quantity):
            dict1 = {'Area': Area.shapes.keys(),
                     'Surface Area': Volume.shapes.keys(),
                     'Volume': Volume.shapes.keys()}
            self.shapeCombo.clear()
            self.shapeCombo.addItems(dict1[quantity])

        def continueFunction(quantity, shape):
            self.calcButton.setHidden(False)
            self.resultFrame.setHidden(False)

            self.label1 = QLabel(self.frame_2)
            self.label2 = QLabel(self.frame_2)
            self.label3 = QLabel(self.frame_2)

            self.labelDict = {0: self.label1,
                              1: self.label2,
                              2: self.label3}

            self.field1 = QLineEdit(self.frame_2)
            self.field1.setValidator(self.onlyInt)
            self.field2 = QLineEdit(self.frame_2)
            self.field2.setValidator(self.onlyInt)
            self.field3 = QLineEdit(self.frame_2)
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
                self.labelDict[f].setStyleSheet('border:0px;color:#A5BABA')
                self.labelDict[f].setFont(QFont("Trebuchet MS", 14))
                self.lineEditDict[f].setFont(QFont("Trebuchet MS", 14))
                self.lineEditDict[f].setStyleSheet(
                    "background-color:#2B2B2B; color:#A5BABA; border:2px outset black;")
                self.fl2.addRow(self.labelDict[f], self.lineEditDict[f])

        def calcFunc():
            values = list()
            quantity = self.quantityCombo.currentText()
            shape = self.shapeCombo.currentText()
            fields = self.frame_2.findChildren(QLineEdit)
            for x in fields:
                if x.objectName() == 'resultFrame':
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
                    self.resultFrame.setText(
                        "Result : " + str(Functions.Connect(quantity, shape, values)))


if __name__ == '__main__':
    app = QApplication(argv)
    mw = MainWindow()
    exit(app.exec_())
