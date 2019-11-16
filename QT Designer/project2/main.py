from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FlightChooser import *
import sys

class App(QDialog):

    def __init__(self):
        
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        fare = ""

        self.ui.BusinessClassRadioButton.toggled.connect(self.changeFare)
        self.ui.EconomyClassRadioButton.toggled.connect(self.changeFare)
        self.ui.firstClassRadioButton.toggled.connect(self.changeFare)
        self.ui.label_2
    
    def changeFare(self):

        if self.ui.firstClassRadioButton.isChecked() == True:
            self.ui.label_2.setText("Fare is $150")
        elif self.ui.BusinessClassRadioButton.isChecked() == True:
            self.ui.label_2.setText("Fare is $125")
        elif self.ui.EconomyClassRadioButton.isChecked() == True:
            self.ui.label_2.setText("Fare is $100")


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())

