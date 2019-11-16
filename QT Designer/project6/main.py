from PyQt4.QtCore import *
from PyQt4.QtGui import *
from SpinBox import *


class App(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        bookPzeEnt = self.ui.BookPriceEnt
        bookQtySpin = self.ui.BookQuantSpin
        bookTleEnt = self.ui.BookTotalEnt

        sugarPzeEnt = self.ui.SugarPriceEnt
        sugarQtySpin = self.ui.SugarQuantSpin
        sugarTleEnt = self.ui.SugarTotalEnt

        bookPzeEnt.setValidator(QDoubleValidator())
        sugarPzeEnt.setValidator(QDoubleValidator())
        sugarTleEnt.setValidator(QDoubleValidator())
        bookTleEnt.setValidator(QDoubleValidator())

        bookPzeEnt.setText(str(0))
        sugarPzeEnt.setText(str(0))

        bookPzeEnt.textChanged.connect(self.calcuate)
        bookQtySpin.valueChanged.connect(self.calcuate)
        bookTleEnt.textChanged.connect(self.calcuate)
        sugarPzeEnt.textChanged.connect(self.calcuate)
        sugarQtySpin.valueChanged.connect(self.calcuate)
        sugarTleEnt.textChanged.connect(self.calcuate)
    
    def calcuate(self):

        bookPzeEnt = self.ui.BookPriceEnt
        bookQtySpin = self.ui.BookQuantSpin
        bookTleEnt = self.ui.BookTotalEnt

        sugarPzeEnt = self.ui.SugarPriceEnt
        sugarQtySpin = self.ui.SugarQuantSpin
        sugarTleEnt = self.ui.SugarTotalEnt

        bookTotal = int(bookPzeEnt.text()) * int(bookQtySpin.text())
        sugarTotal = float(sugarPzeEnt.text()) * float(sugarQtySpin.text())

        bookTleEnt.setText(str(bookTotal))
        sugarTleEnt.setText(str(sugarTotal))

        grandTotal = bookTotal + sugarTotal
        self.ui.GrandTotalLabel.setText("Grand Total : "+str(grandTotal))



if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()