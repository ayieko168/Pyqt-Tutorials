# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\project2\FlightChooser.ui'
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
        Dialog.resize(400, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.firstClassRadioButton = QtGui.QRadioButton(Dialog)
        self.firstClassRadioButton.setGeometry(QtCore.QRect(30, 70, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstClassRadioButton.setFont(font)
        self.firstClassRadioButton.setObjectName(_fromUtf8("firstClassRadioButton"))
        self.BusinessClassRadioButton = QtGui.QRadioButton(Dialog)
        self.BusinessClassRadioButton.setGeometry(QtCore.QRect(30, 100, 241, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BusinessClassRadioButton.setFont(font)
        self.BusinessClassRadioButton.setObjectName(_fromUtf8("BusinessClassRadioButton"))
        self.EconomyClassRadioButton = QtGui.QRadioButton(Dialog)
        self.EconomyClassRadioButton.setGeometry(QtCore.QRect(30, 130, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EconomyClassRadioButton.setFont(font)
        self.EconomyClassRadioButton.setObjectName(_fromUtf8("EconomyClassRadioButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Flight Chooser", None))
        self.label.setText(_translate("Dialog", "Choose The Flight", None))
        self.firstClassRadioButton.setText(_translate("Dialog", "First Class $150", None))
        self.BusinessClassRadioButton.setText(_translate("Dialog", "Bussiness Class    $125", None))
        self.EconomyClassRadioButton.setText(_translate("Dialog", "Economy Class   $100", None))
        self.label_2.setText(_translate("Dialog", "TextLabel", None))

