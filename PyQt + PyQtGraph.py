from PyQt4 import QtGui # (the example applies equally well to PySide)
import pyqtgraph as pg
import numpy as np

## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()

## Create some widgets to be placed inside
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()
#####################
x = np.arange(1000)
y = np.random.normal(size=(3, 1000))
plotWidget = pg.plot(title="Three plot curves")
for i in range(3):
    plotWidget.plot(x, y[i], pen=(i,3)) ## setting pen=(i,3) automaticaly creates three different-colored pens
####################
plot = pg.PlotWidget()

## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0) # button goes in upper-left
layout.addWidget(text, 1, 0) # text edit goes in middle-left
layout.addWidget(listw, 2, 0) # list widget goes in bottom-left
layout.addWidget(plotWidget, 0, 1, 3, 1) # plot goes on right side, spanning 3 rows

## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
