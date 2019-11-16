# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(270, 203)
        self.CalculateButton = QtGui.QPushButton(Frame)
        self.CalculateButton.setGeometry(QtCore.QRect(100, 110, 91, 23))
        self.CalculateButton.setObjectName(_fromUtf8("CalculateButton"))
        self.lineEditVal1 = QtGui.QLineEdit(Frame)
        self.lineEditVal1.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.lineEditVal1.setObjectName(_fromUtf8("lineEditVal1"))
        self.lineEditVal2 = QtGui.QLineEdit(Frame)
        self.lineEditVal2.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEditVal2.setObjectName(_fromUtf8("lineEditVal2"))
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 47, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 47, 13))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.CalculateButton.setText(_translate("Frame", "Calculate!", None))
        self.label.setText(_translate("Frame", "Input 1", None))
        self.label_2.setText(_translate("Frame", "Input 2", None))
        self.label_3.setText(_translate("Frame", "Answer is :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

