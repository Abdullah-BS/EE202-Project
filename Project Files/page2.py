# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2-final-maybe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2000,2000)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color:rgb(222, 250, 255)")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(1500, 900))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Neo Sans W23 Bold")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Neo Sans W23 Bold")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_P2_AddSem = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3000)
        sizePolicy.setVerticalStretch(1000)
        sizePolicy.setHeightForWidth(self.pushButton_P2_AddSem.sizePolicy().hasHeightForWidth())
        self.pushButton_P2_AddSem.setSizePolicy(sizePolicy)
        self.pushButton_P2_AddSem.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButton_P2_AddSem.setFont(font)
        self.pushButton_P2_AddSem.setStyleSheet("border: 2px solid;\n"
"border-radius: 10px;\n"
"background-color:rgb(98, 98, 98);\n"
"color: rgb(222, 250, 255);")
        self.pushButton_P2_AddSem.setObjectName("pushButton_P2_AddSem")
        self.verticalLayout_3.addWidget(self.pushButton_P2_AddSem)
        self.pushButton_P2_AddSem_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_P2_AddSem_2.sizePolicy().hasHeightForWidth())
        self.pushButton_P2_AddSem_2.setSizePolicy(sizePolicy)
        self.pushButton_P2_AddSem_2.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButton_P2_AddSem_2.setFont(font)
        self.pushButton_P2_AddSem_2.setStyleSheet("border: 2px solid;\n"
"border-radius: 10px;\n"
"background-color:rgb(98, 98, 98);\n"
"color: rgb(222, 250, 255);")
        self.pushButton_P2_AddSem_2.setObjectName("pushButton_P2_AddSem_2")
        self.verticalLayout_3.addWidget(self.pushButton_P2_AddSem_2)
        self.pushButton_P2_EditSem = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_P2_EditSem.sizePolicy().hasHeightForWidth())
        self.pushButton_P2_EditSem.setSizePolicy(sizePolicy)
        self.pushButton_P2_EditSem.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButton_P2_EditSem.setFont(font)
        self.pushButton_P2_EditSem.setStyleSheet("border: 2px solid;\n"
"border-radius: 10px;\n"
"background-color:rgb(98, 98, 98);\n"
"color: rgb(222, 250, 255);")
        self.pushButton_P2_EditSem.setObjectName("pushButton_P2_EditSem")
        self.verticalLayout_3.addWidget(self.pushButton_P2_EditSem)
        self.comboBox_P2 = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_P2.sizePolicy().hasHeightForWidth())
        self.comboBox_P2.setSizePolicy(sizePolicy)
        self.comboBox_P2.setMaximumSize(QtCore.QSize(300, 70))
        self.comboBox_P2.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBox_P2.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Neo Sans W23 Bold")
        font.setPointSize(10)
        self.comboBox_P2.setFont(font)
        self.comboBox_P2.setStyleSheet("border: 2px solid;\n"
"border-radius: 10px;\n"
"    font-size: 28px;\n"
"background-color:rgb(98, 98, 98);\n"
"color: rgb(222, 250, 255);")
        self.comboBox_P2.setObjectName("comboBox_P2")
        self.comboBox_P2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_P2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(98, 98, 98);")
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QtCore.QSize(700,70))
        self.verticalLayout_4.addWidget(self.label_2)
        self.pushButton_P2_Add = QtWidgets.QPushButton(self.frame)
        self.pushButton_P2_Add.setEnabled(True)
        self.pushButton_P2_Add.setMaximumSize(QtCore.QSize(300,70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(300)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.pushButton_P2_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_P2_Add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_P2_Add.setFont(font)
        self.pushButton_P2_Add.setStyleSheet("QPushButton {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(222, 250, 255);\n"
"    border: 1px solid;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"\n"
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
        self.pushButton_P2_Add.setObjectName("pushButton_P2_Add")
        self.verticalLayout_4.addWidget(self.pushButton_P2_Add)
        self.pushButton_P2_Add_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_P2_Add_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_P2_Add_2.sizePolicy().hasHeightForWidth())
        self.pushButton_P2_Add_2.setSizePolicy(sizePolicy)
        self.pushButton_P2_Add_2.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_P2_Add_2.setFont(font)
        self.pushButton_P2_Add_2.setStyleSheet("QPushButton {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(222, 250, 255);\n"
"    border: 1px solid;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"\n"
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
        self.pushButton_P2_Add_2.setObjectName("pushButton_P2_Add_2")
        self.verticalLayout_4.addWidget(self.pushButton_P2_Add_2)
        self.pushButton_P2_Edit = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_P2_Edit.sizePolicy().hasHeightForWidth())
        self.pushButton_P2_Edit.setSizePolicy(sizePolicy)
        self.pushButton_P2_Edit.setMaximumSize(QtCore.QSize(300, 70))
        self.pushButton_P2_Edit.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_P2_Edit.setFont(font)
        self.pushButton_P2_Edit.setStyleSheet("QPushButton {\n"
"    background-color:rgb(153, 153, 153);\n"
"    color:rgb(222, 250, 255);\n"
"    border: 1px solid;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"\n"
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
        self.pushButton_P2_Edit.setObjectName("pushButton_P2_Edit")
        self.verticalLayout_4.addWidget(self.pushButton_P2_Edit)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(98, 98, 98);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Neo Sans W23 Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(98, 98, 98);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 8px;\n"
"border: 0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(98, 98, 98);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 8px;\n"
"border: 0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.tableWidget_P2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_P2.setStyleSheet("QTableWidget {\n"
"    background-color:rgb(248, 248, 248); /* Background color of the table */\n"
"    selection-background-color: rgb(153, 153, 153); /* Background color when a cell is selected */\n"
"    gridline-color: rgb(153, 153, 153); /* Color of gridlines */\n"
"\n"
"    /* Optional: Set other properties */\n"
"    color: rgb(98, 98, 98); /* Text color */\n"
"    font-size: 12pt; /* Font size */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px; /* Padding for cell content */\n"
"    border-bottom: 2px solid #d0d0d0; /* Border between rows */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #a6a6a6; /* Background color of selected cell */\n"
"    color: #ffffff; /* Text color of selected cell */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:rgb(98, 98, 98); /* Background color of header sections */\n"
"    color: #ffffff; /* Text color of header sections */\n"
# "    padding: 6px; /* Padding for header sections */\n"
"    border: 2px solid #ffffff; /* Border around header sections */\n"
"    font-size: 12pt; /* Set your desired font size */\n"
"font-family: Neo Sans W23 Bold;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    border: 1px solid rgb(0, 0, 0); /* Border at the bottom of the header */\n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    border: 1px solid rgb(0, 0, 0); /* Border on the right of the header */\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader::section,\n"
"QTableWidget::verticalHeader::section {\n"
"    border: 1px solid #ffffff; /* Border around header sections */\n"
"}")
        self.tableWidget_P2.setObjectName("tableWidget_P2")
        self.tableWidget_P2.setColumnCount(6)
        self.tableWidget_P2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_P2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_P2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_P2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_P2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_P2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_P2.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableWidget_P2, 3, 1, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.tableWidget_P2.setRowCount(1)
        self.tableWidget_P2.setColumnWidth(0,390)
        self.tableWidget_P2.setColumnWidth(1,200)
        self.tableWidget_P2.setColumnWidth(2,200)
        self.tableWidget_P2.setColumnWidth(3,130)
        self.tableWidget_P2.setColumnWidth(4,100)
        self.tableWidget_P2.setColumnWidth(5,100)
        self.tableWidget_P2.horizontalHeader().setStretchLastSection(True)

        self.comboBox_P2.setEditable(True)
        self.comboBox_P2.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "Confirm"))
        self.pushButton_P2_AddSem.setText(_translate("Form", "Add Semester"))
        self.pushButton_P2_AddSem_2.setText(_translate("Form", "Remove Semester"))
        self.pushButton_P2_EditSem.setText(_translate("Form", "Edit Semester"))
        self.comboBox_P2.setItemText(0, _translate("Form", "--Semester"))
        self.label_2.setText(_translate("Form", "Course Options:"))
        self.pushButton_P2_Add.setText(_translate("Form", "Add Course"))
        self.pushButton_P2_Add_2.setText(_translate("Form", "Remove Course"))
        self.pushButton_P2_Edit.setText(_translate("Form", "Edit Course"))
        self.label_5.setText(_translate("Form", "Personal Information"))
        self.label_3.setText(_translate("Form", "Name:"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Your Name"))
        self.label_4.setText(_translate("Form", "ID"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "ex. 2222222"))
        item = self.tableWidget_P2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Course Title"))
        item = self.tableWidget_P2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Course Name"))
        item = self.tableWidget_P2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Reference Number"))
        item = self.tableWidget_P2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Credit Hours"))
        item = self.tableWidget_P2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Mark"))
        item = self.tableWidget_P2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Grade"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())