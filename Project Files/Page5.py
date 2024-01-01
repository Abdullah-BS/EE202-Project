# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page555.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 508)
        Form.setStyleSheet("background-color: rgb(222, 250, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color:rgb(222, 250, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(98, 98, 98);")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)
        self.lineEdit_P5_SName = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_P5_SName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_P5_SName.sizePolicy().hasHeightForWidth())
        self.lineEdit_P5_SName.setSizePolicy(sizePolicy)
        self.lineEdit_P5_SName.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lineEdit_P5_SName.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_P5_SName.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_P5_SName.setFont(font)
        self.lineEdit_P5_SName.setStyleSheet("border-radius: 8px;\n"
"border: 0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_P5_SName.setObjectName("lineEdit_P5_SName")
        self.gridLayout_3.addWidget(self.lineEdit_P5_SName, 0, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_P5_Cancel = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_P5_Cancel.setFont(font)
        self.pushButton_P5_Cancel.setStyleSheet("QPushButton {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(222, 250, 255);\n"
"    border: 1px solid;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(0, 0, 0);}")
        self.pushButton_P5_Cancel.setObjectName("pushButton_P5_Cancel")
        self.gridLayout_2.addWidget(self.pushButton_P5_Cancel, 1, 1, 1, 1)
        self.pushButton_P5_Add = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_P5_Add.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_P5_Add.setFont(font)
        self.pushButton_P5_Add.setStyleSheet("QPushButton {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(222, 250, 255);\n"
"    border: 1px solid;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 28px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(0, 0, 0);}")
        self.pushButton_P5_Add.setObjectName("pushButton_P5_Add")
        self.gridLayout_2.addWidget(self.pushButton_P5_Add, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Semester Name: "))
        self.lineEdit_P5_SName.setText(_translate("Form", ""))
        self.lineEdit_P5_SName.setPlaceholderText(_translate("Form", "Ex. Fall-2023"))
        self.pushButton_P5_Cancel.setText(_translate("Form", "Cancel"))
        self.pushButton_P5_Add.setText(_translate("Form", "Add"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())