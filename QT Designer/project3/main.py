from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GroupingRadioButtons import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

selectedSize = ""
selectedPay = ""


class App(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.mSizeRadio.toggled.connect(self.setSHirtSize)
        self.ui.lSizeRadio.toggled.connect(self.setSHirtSize)
        self.ui.xlSizeRadio_2.toggled.connect(self.setSHirtSize)
        self.ui.xxlSizeRadio_2.toggled.connect(self.setSHirtSize)

        self.ui.debitCreditRadio.toggled.connect(self.setSHirtSize)
        self.ui.netBankingRadio.toggled.connect(self.setSHirtSize)
        self.ui.cashOnDeliveryRadio.toggled.connect(self.setSHirtSize)

    def setSHirtSize(self):

        global selectedPay, selectedSize

        if self.ui.mSizeRadio.isChecked() == True:
            selectedSize = "M"
        if self.ui.lSizeRadio.isChecked() == True:
            selectedSize = "L"
        if self.ui.xlSizeRadio_2.isChecked() == True:
            selectedSize = "XL"
        if self.ui.xxlSizeRadio_2.isChecked() == True:
            selectedSize = "XXL"

        if self.ui.debitCreditRadio.isChecked() == True:
            selectedPay = "Debit/Credit Card"
        if self.ui.netBankingRadio.isChecked() == True:
            selectedSize = "Net Banking"
        if self.ui.cashOnDeliveryRadio.isChecked() == True:
            selectedSize = " Cash on delivery"

        t = "Choosen Shirt Size is {} and Payment Methd Is {}".format(selectedSize, selectedPay)
        print(t)
        self.ui.resultLabel.setText(t)


if __name__ == "__main__":

    w = QApplication([])
    Application = App()
    Application.show()
    w.exec_()
