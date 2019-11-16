from PyQt4.QtCore import *
from PyQt4.QtGui import *
from SimpleCalculator import *

class App(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.FistNumberLineEdit.setText("0")
        self.ui.SecondNumberLineEdit.setText("0")

        self.ui.AddpushButton.clicked.connect(self.summation)
        self.ui.SubpushButton.clicked.connect(self.subtraction)
        self.ui.MultiplypushButton.clicked.connect(self.multiplication)
        self.ui.DividepushButton.clicked.connect(self.divition)


    def summation(self):

        num1 = self.ui.FistNumberLineEdit.text()
        num2 = self.ui.SecondNumberLineEdit.text()
    
        resalt = int(num1) + int(num2)
        self.ui.Resultlabel.setText("ADDITION :"+str(resalt))

    def subtraction(self):

        num1 = self.ui.FistNumberLineEdit.text()
        num2 = self.ui.SecondNumberLineEdit.text()
    
        resalt = int(num1) - int(num2)
        self.ui.Resultlabel.setText("SUBTRACTION :"+str(resalt))

    def multiplication(self):

        num1 = self.ui.FistNumberLineEdit.text()
        num2 = self.ui.SecondNumberLineEdit.text()
    
        resalt = int(num1) * int(num2)
        self.ui.Resultlabel.setText("MULTIPLICATION :"+str(resalt))

    def divition(self):

        num1 = self.ui.FistNumberLineEdit.text()
        num2 = self.ui.SecondNumberLineEdit.text()

        try:
            resalt = int(num1) / int(num2)
            self.ui.Resultlabel.setText("DIVITION :"+str(resalt))
        except ZeroDivisionError:
            self.ui.Resultlabel.setText("ZERO DIVITION ERROR")



if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()
