# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/PyQt Tutorials/QT Designer/project3/GroupingRadioButtons.ui'
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
        Dialog.resize(319, 430)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 161, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mSizeRadio = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.mSizeRadio.setObjectName(_fromUtf8("mSizeRadio"))
        self.verticalLayout.addWidget(self.mSizeRadio)
        self.lSizeRadio = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.lSizeRadio.setObjectName(_fromUtf8("lSizeRadio"))
        self.verticalLayout.addWidget(self.lSizeRadio)
        self.xlSizeRadio_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.xlSizeRadio_2.setObjectName(_fromUtf8("xlSizeRadio_2"))
        self.verticalLayout.addWidget(self.xlSizeRadio_2)
        self.xxlSizeRadio_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.xxlSizeRadio_2.setObjectName(_fromUtf8("xxlSizeRadio_2"))
        self.verticalLayout.addWidget(self.xxlSizeRadio_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 240, 160, 88))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.debitCreditRadio = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.debitCreditRadio.setObjectName(_fromUtf8("debitCreditRadio"))
        self.verticalLayout_2.addWidget(self.debitCreditRadio)
        self.netBankingRadio = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.netBankingRadio.setObjectName(_fromUtf8("netBankingRadio"))
        self.verticalLayout_2.addWidget(self.netBankingRadio)
        self.cashOnDeliveryRadio = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.cashOnDeliveryRadio.setObjectName(_fromUtf8("cashOnDeliveryRadio"))
        self.verticalLayout_2.addWidget(self.cashOnDeliveryRadio)
        self.Title = QtGui.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(80, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.chooseShirtTitle = QtGui.QLabel(Dialog)
        self.chooseShirtTitle.setGeometry(QtCore.QRect(30, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chooseShirtTitle.setFont(font)
        self.chooseShirtTitle.setObjectName(_fromUtf8("chooseShirtTitle"))
        self.choosePaymentTitle = QtGui.QLabel(Dialog)
        self.choosePaymentTitle.setGeometry(QtCore.QRect(30, 220, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choosePaymentTitle.setFont(font)
        self.choosePaymentTitle.setObjectName(_fromUtf8("choosePaymentTitle"))
        self.resultLabel = QtGui.QLabel(Dialog)
        self.resultLabel.setGeometry(QtCore.QRect(120, 360, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resultLabel.setFont(font)
        self.resultLabel.setText(_fromUtf8(""))
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.mSizeRadio.setText(_translate("Dialog", "M", None))
        self.lSizeRadio.setText(_translate("Dialog", "L", None))
        self.xlSizeRadio_2.setText(_translate("Dialog", "XL", None))
        self.xxlSizeRadio_2.setText(_translate("Dialog", "XXL", None))
        self.debitCreditRadio.setText(_translate("Dialog", "Debit/Credit Card", None))
        self.netBankingRadio.setText(_translate("Dialog", "Net Banking", None))
        self.cashOnDeliveryRadio.setText(_translate("Dialog", "Cash On Delicery", None))
        self.Title.setText(_translate("Dialog", "Buy A Shirt Dot Com", None))
        self.chooseShirtTitle.setText(_translate("Dialog", "Choose Your Shirt Size", None))
        self.choosePaymentTitle.setText(_translate("Dialog", "Choose Your Payment Method", None))

