# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\royal state\PycharmProjects\PyQt Tutorials\QT Designer\project4\Events.ui'
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
        Dialog.resize(274, 338)
        self.CopyPushButton = QtGui.QPushButton(Dialog)
        self.CopyPushButton.setGeometry(QtCore.QRect(80, 80, 101, 23))
        self.CopyPushButton.setObjectName(_fromUtf8("CopyPushButton"))
        self.copyLineEdit = QtGui.QLineEdit(Dialog)
        self.copyLineEdit.setGeometry(QtCore.QRect(60, 30, 151, 20))
        self.copyLineEdit.setObjectName(_fromUtf8("copyLineEdit"))
        self.PasteLineEdit = QtGui.QLineEdit(Dialog)
        self.PasteLineEdit.setGeometry(QtCore.QRect(60, 130, 151, 20))
        self.PasteLineEdit.setObjectName(_fromUtf8("PasteLineEdit"))
        self.pastePushButton = QtGui.QPushButton(Dialog)
        self.pastePushButton.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.pastePushButton.setObjectName(_fromUtf8("pastePushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pastePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.PasteLineEdit.paste)
        QtCore.QObject.connect(self.CopyPushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.copyLineEdit.selectAll)
        QtCore.QObject.connect(self.CopyPushButton, QtCore.SIGNAL(_fromUtf8("released()")), self.copyLineEdit.copy)
        QtCore.QObject.connect(self.pastePushButton, QtCore.SIGNAL(_fromUtf8("released()")), self.PasteLineEdit.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.CopyPushButton.setText(_translate("Dialog", "COPY", None))
        self.pastePushButton.setText(_translate("Dialog", "PASTE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

