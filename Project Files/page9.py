# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page9.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1189)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1920, 1080))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color: rgb(222, 250, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setMinimumSize(QtCore.QSize(1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Cover Page.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(800, 460, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Neo Sans W23")
        font.setPointSize(27)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"background-color:rgb(98, 98, 98);\n"
"color: rgb(222, 250, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgb(98, 98, 98);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
