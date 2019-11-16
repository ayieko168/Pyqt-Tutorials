# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\project1\demoLineEdit.ui'
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
        Dialog.resize(360, 198)
        self.labelResponse = QtGui.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 80, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelResponse.setFont(font)
        self.labelResponse.setText(_fromUtf8(""))
        self.labelResponse.setObjectName(_fromUtf8("labelResponse"))
        self.lineEditName = QtGui.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(100, 30, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ButtonClickMe = QtGui.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(110, 130, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonClickMe.setFont(font)
        self.ButtonClickMe.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.ButtonClickMe.setToolTip(_fromUtf8(""))
        self.ButtonClickMe.setWhatsThis(_fromUtf8(""))
        self.ButtonClickMe.setObjectName(_fromUtf8("ButtonClickMe"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Hello World", None))
        self.label_2.setText(_translate("Dialog", "Enter Your Name", None))
        self.ButtonClickMe.setText(_translate("Dialog", "Click", None))

