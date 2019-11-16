import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class tooldemo(QMainWindow):
   def __init__(self, parent = None):
      super(tooldemo, self).__init__(parent)
      layout = QVBoxLayout()
		
      btn = QPushButton(self, text="Hello")
      btn.clicked.connect(self.clickCMD)
      self.setLayout(layout)
      self.setWindowTitle("toolbar demo")
		
   def clickCMD(self):
      print ("pressed button is")

      # show message box
      msg = QMessageBox()
      msg.setText("Path Copied To clipboard!")
      msg.setWindowTitle("INFORMATION")
      msg.setIcon(QMessageBox.Information)
      msg.setDetailedText("This is the detailed section")
      msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      msgVal = msg.exec_()

      print(msgVal)
		
def main():
   app = QApplication(sys.argv)
   ex = tooldemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
