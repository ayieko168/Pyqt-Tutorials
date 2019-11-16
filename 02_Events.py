from PyQt4.QtGui import *

App = QApplication([])

MainWidg = QWidget()
layout = QGridLayout()
MainWidg.setLayout(layout)

btn1 = QPushButton("Button 1")
btn1.clicked.connect(lambda: print("Clicked!"))
layout.addWidget(btn1, 0, 0)

MainWidg.show()

App.exec_()
