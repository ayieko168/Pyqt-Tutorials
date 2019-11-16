# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\project6\SpinBox.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(513, 219)
        Dialog.setAcceptDrops(False)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.BookPriceEnt = QtGui.QLineEdit(Dialog)
        self.BookPriceEnt.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.BookPriceEnt.setObjectName(_fromUtf8("BookPriceEnt"))
        self.BookQuantSpin = QtGui.QSpinBox(Dialog)
        self.BookQuantSpin.setGeometry(QtCore.QRect(251, 50, 71, 22))
        self.BookQuantSpin.setObjectName(_fromUtf8("BookQuantSpin"))
        self.BookTotalEnt = QtGui.QLineEdit(Dialog)
        self.BookTotalEnt.setGeometry(QtCore.QRect(350, 50, 113, 21))
        self.BookTotalEnt.setObjectName(_fromUtf8("BookTotalEnt"))
        self.SugarTotalEnt = QtGui.QLineEdit(Dialog)
        self.SugarTotalEnt.setGeometry(QtCore.QRect(350, 100, 113, 21))
        self.SugarTotalEnt.setObjectName(_fromUtf8("SugarTotalEnt"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.SugarPriceEnt = QtGui.QLineEdit(Dialog)
        self.SugarPriceEnt.setGeometry(QtCore.QRect(110, 100, 113, 20))
        self.SugarPriceEnt.setObjectName(_fromUtf8("SugarPriceEnt"))
        self.SugarQuantSpin = QtGui.QDoubleSpinBox(Dialog)
        self.SugarQuantSpin.setGeometry(QtCore.QRect(240, 100, 81, 22))
        self.SugarQuantSpin.setObjectName(_fromUtf8("SugarQuantSpin"))
        self.GrandTotalLabel = QtGui.QLabel(Dialog)
        self.GrandTotalLabel.setGeometry(QtCore.QRect(140, 160, 251, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setPointSize(12)
        self.GrandTotalLabel.setFont(font)
        self.GrandTotalLabel.setText(_fromUtf8(""))
        self.GrandTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GrandTotalLabel.setObjectName(_fromUtf8("GrandTotalLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Price Calculator", None))
        self.label.setText(_translate("Dialog", "Book Price", None))
        self.label_2.setText(_translate("Dialog", "Sugar Price", None))

