# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\project7\scrollbarsAndAcales.ui'
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
        Dialog.resize(539, 441)
        self.SugarLevelScrollBar = QtGui.QScrollBar(Dialog)
        self.SugarLevelScrollBar.setGeometry(QtCore.QRect(180, 41, 291, 20))
        self.SugarLevelScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.SugarLevelScrollBar.setObjectName(_fromUtf8("SugarLevelScrollBar"))
        self.BloodPressureSlider = QtGui.QSlider(Dialog)
        self.BloodPressureSlider.setGeometry(QtCore.QRect(180, 90, 281, 21))
        self.BloodPressureSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BloodPressureSlider.setObjectName(_fromUtf8("BloodPressureSlider"))
        self.PulseRateScrollBar = QtGui.QScrollBar(Dialog)
        self.PulseRateScrollBar.setGeometry(QtCore.QRect(180, 150, 16, 160))
        self.PulseRateScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.PulseRateScrollBar.setObjectName(_fromUtf8("PulseRateScrollBar"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(6)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setIndent(6)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(226, 150, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.CholestrolSlider = QtGui.QSlider(Dialog)
        self.CholestrolSlider.setGeometry(QtCore.QRect(360, 149, 20, 171))
        self.CholestrolSlider.setOrientation(QtCore.Qt.Vertical)
        self.CholestrolSlider.setObjectName(_fromUtf8("CholestrolSlider"))
        self.ResultEntry = QtGui.QLineEdit(Dialog)
        self.ResultEntry.setGeometry(QtCore.QRect(60, 350, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultEntry.setFont(font)
        self.ResultEntry.setObjectName(_fromUtf8("ResultEntry"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Scrollbar Scale Test", None))
        self.label_2.setText(_translate("Dialog", "Sugar Level", None))
        self.label_3.setText(_translate("Dialog", "Blood Presure", None))
        self.label_4.setText(_translate("Dialog", "Pulse Rate", None))
        self.label_5.setText(_translate("Dialog", "Cholestrol Level", None))

