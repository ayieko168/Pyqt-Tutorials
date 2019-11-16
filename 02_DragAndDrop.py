"""
Enter Some Text In the entry field and
drag it to the dropdown menu
to add it to the list.
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class combo(QComboBox):

   def __init__(self, title, parent):
      super(combo, self).__init__( parent)
	
      self.setAcceptDrops(True)
		
   def dragEnterEvent(self, e):
      print (e)
		
      if e.mimeData().hasText():
         e.accept()
      else:
         e.ignore()
			
   def dropEvent(self, e):
      self.addItem(e.mimeData().text())
		
class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()
		
      self.initUI()
		
   def initUI(self):
      lo = QFormLayout()
      lo.addRow(QLabel("Type some text in textbox and drag it into combo box"))
		
      edit = QLineEdit()
      edit.setDragEnabled(True)
      com = combo("Button", self)
      lo.addRow(edit,com)
      self.setLayout(lo)
      self.setWindowTitle('Simple drag & drop')
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   ex.show()
   app.exec_()
	
if __name__ == '__main__':
   main()
