# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\project5\SimpleCalculator.ui'
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
        Dialog.resize(361, 296)
        self.FistNumberLineEdit = QtGui.QLineEdit(Dialog)
        self.FistNumberLineEdit.setGeometry(QtCore.QRect(160, 50, 131, 21))
        self.FistNumberLineEdit.setObjectName(_fromUtf8("FistNumberLineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.AddpushButton = QtGui.QPushButton(Dialog)
        self.AddpushButton.setGeometry(QtCore.QRect(50, 140, 41, 31))
        self.AddpushButton.setObjectName(_fromUtf8("AddpushButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.SecondNumberLineEdit = QtGui.QLineEdit(Dialog)
        self.SecondNumberLineEdit.setGeometry(QtCore.QRect(160, 90, 131, 21))
        self.SecondNumberLineEdit.setObjectName(_fromUtf8("SecondNumberLineEdit"))
        self.Resultlabel = QtGui.QLabel(Dialog)
        self.Resultlabel.setGeometry(QtCore.QRect(60, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Resultlabel.setFont(font)
        self.Resultlabel.setText(_fromUtf8(""))
        self.Resultlabel.setObjectName(_fromUtf8("Resultlabel"))
        self.SubpushButton = QtGui.QPushButton(Dialog)
        self.SubpushButton.setGeometry(QtCore.QRect(110, 140, 41, 31))
        self.SubpushButton.setObjectName(_fromUtf8("SubpushButton"))
        self.MultiplypushButton = QtGui.QPushButton(Dialog)
        self.MultiplypushButton.setGeometry(QtCore.QRect(170, 140, 41, 31))
        self.MultiplypushButton.setObjectName(_fromUtf8("MultiplypushButton"))
        self.DividepushButton = QtGui.QPushButton(Dialog)
        self.DividepushButton.setGeometry(QtCore.QRect(230, 140, 41, 31))
        self.DividepushButton.setObjectName(_fromUtf8("DividepushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Enter First Number", None))
        self.AddpushButton.setText(_translate("Dialog", "+", None))
        self.label_2.setText(_translate("Dialog", "Enter Second Number", None))
        self.SubpushButton.setText(_translate("Dialog", "-", None))
        self.MultiplypushButton.setText(_translate("Dialog", "*", None))
        self.DividepushButton.setText(_translate("Dialog", "/", None))

