from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

from PyQt5.QtGui import QTextDocument 

import sys

from stu import Student as Stu

from Class_Semester import Semester as Sem

from Course import Course as Crs

from page1 import Ui_Form as p1

from page2 import Ui_Form as p2

from page3 import Ui_Form as p3

from Page4 import Ui_Form as p4

from Page5 import Ui_Form as p5

from Page7_UI_page_same_as_page4  import Ui_Form as p7

from page8 import Ui_Form as p8

from page9 import Ui_Dialog as p9

from page10 import Ui_Form as p10


class Main:
    
    
    
    def Widget(self):
        
        # code for page 1 GUI
        
        self.P1_Form = QtWidgets.QWidget()
        self.P1_ui = p1()
        self.P1_ui.setupUi(self.P1_Form)
        self.P1_Form.show()
        # self.P1_ui.tableWidget_P1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        

        
        
        
        # code for page 2 gui
        self.P2_Form = QtWidgets.QWidget()
        self.P2_ui = p2()
        self.P2_ui.setupUi(self.P2_Form)
        self.P2_ui.tableWidget_P2.setColumnCount(6)
       
        
        
        
        
        
        
        
        
        
        # code for page 3 gui
        
        self.P3_Form = QtWidgets.QWidget()
        self.P3_ui = p3()
        self.P3_ui.setupUi(self.P3_Form)
        
        self.P3_ui.tableWidget_P3.setColumnWidth(0,700)
        self.P3_ui.tableWidget_P3.setColumnWidth(1,210)
        self.P3_ui.tableWidget_P3.setColumnWidth(2,225)
        self.P3_ui.tableWidget_P3.setColumnWidth(3,150)
        self.P3_ui.tableWidget_P3.setColumnWidth(4,100)
        self.P3_ui.tableWidget_P3.setColumnWidth(5,100)
        
        # code for page 4 gui
        
        self.P4_Form = QtWidgets.QWidget()
        self.P4_ui = p4()
        self.P4_ui.setupUi(self.P4_Form)
        
        
        # code for page 5 gui
        self.P5_Form = QtWidgets.QWidget()
        self.P5_ui = p5()
        self.P5_ui.setupUi(self.P5_Form)
        
        
        
        # code for page 7 gui
        self.P7_Form = QtWidgets.QWidget()
        self.P7_ui = p7()
        self.P7_ui.setupUi(self.P7_Form)
        
        # code for page 8 gui
        self.P8_Form = QtWidgets.QWidget()
        self.P8_ui = p8()
        self.P8_ui.setupUi(self.P8_Form)
        
        # code for page 9 gui
        self.P9_Dialog = QtWidgets.QDialog()
        self.P9_ui = p9()
        self.P9_ui.setupUi(self.P9_Dialog)
        # self.P9_Dialog.show()

        # code for page 8 gui
        self.P10_Form = QtWidgets.QWidget()
        self.P10_ui = p10()
        self.P10_ui.setupUi(self.P10_Form)
        
        
        # code for stacked layout
        self.layout = QtWidgets.QStackedWidget()
        self.layout.addWidget(self.P1_Form)
        self.layout.addWidget(self.P2_Form)
        self.layout.addWidget(self.P3_Form)
        self.layout.addWidget(self.P4_Form)
        self.layout.addWidget(self.P5_Form)
        self.layout.addWidget(self.P7_Form)
        self.layout.addWidget(self.P8_Form)
        self.layout.addWidget(self.P10_Form)
        self.layout.addWidget(self.P9_Dialog)
        self.layout.setMinimumHeight(1080)
        self.layout.setMinimumWidth(1920)
        self.layout.setCurrentIndex(8) 
        self.layout.show()
        
        
        self.P2_ui.tableWidget_P2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.P1_ui.tableWidget_P1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.P3_ui.tableWidget_P3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        
        
      

       
        
        
        # important objects to be initialized at the start of the program 
        
        
        
        self.SelectedStudentSems = []
          
        self.NewStudentSems = []
        
        self.Students_list = [] # list of students objects 
        
        self.Details_Semesters = []
        
        self.isItemSelected_P1 = False
        
        self.isItemSelected_P2 = False
        
        self.isItemSelected_P3 = False
        
        self.IsEditPage = False
        

        
        
    
        
        
        
        
        
       # Codes related to constant checking/updating
        

        self.P1_ui.tableWidget_P1.itemSelectionChanged.connect(self.CheckForSelectedItems_P1)
        self.P1_ui.tableWidget_P1.itemSelectionChanged.connect(self.CheckForStudents)
        self.P1_ui.tableWidget_P1.itemSelectionChanged.connect(self.StudentIndex)
        
        self.P2_ui.tableWidget_P2.itemSelectionChanged.connect(self.CheckSelectedItems_P2)
        self.P2_ui.tableWidget_P2.itemSelectionChanged.connect(self.CheckForCourses)
        self.P2_ui.lineEdit.textChanged.connect(self.CheckForStudentInfo)
        self.P2_ui.lineEdit_2.textChanged.connect(self.CheckForStudentInfo)
        self.P2_ui.tableWidget_P2.itemSelectionChanged.connect(self.CourseIndex_P2)
        self.P2_ui.comboBox_P2.currentIndexChanged.connect(self.UpdateTableCourses)
        
        
        self.P3_ui.tableWidget_P3.itemSelectionChanged.connect(self.CheckSelectedItems_P3)
        self.P3_ui.tableWidget_P3.itemSelectionChanged.connect(self.CheckForCourses)
        self.P3_ui.comboBox_P3.currentIndexChanged.connect(self.UpdateTableCourses)
        self.P3_ui.tableWidget_P3.itemSelectionChanged.connect(self.CourseIndex_P3)
        
        
        self.P9_ui.pushButton.clicked.connect(self.Show_P1)
        
        
        self.P10_ui.comboBox_P10.currentIndexChanged.connect(self.update_student_info)

        self.CheckForStudents()
        
        
       

        
        
      
        
        

        
        


    def starter(self):

        
        
        self.app = QtWidgets.QApplication(sys.argv)

       
        self.Widget()
        self.clicked()
    
       
        sys.exit(self.app.exec_())



    ############################################
    ###### Code Related to Button clicks  ######
    ############################################
    
    
    
    def clicked(self):


        self.P1_ui.pushButton_P1_Edit_2.clicked.connect(self.Show_P2)
        self.P1_ui.pushButton_P1_Edit.clicked.connect(self.Show_P3)
        self.P1_ui.pushButton_P1_Edit.clicked.connect(self.EditPageOpened)
        self.P1_ui.pushButton_P1_Edit_2.clicked.connect(self.CheckForCourses)
        self.P1_ui.pushButton_P1_Edit.clicked.connect(self.CheckForCourses)
        self.P1_ui.pushButton_P1_Edit.clicked.connect(self.CheckForSemesters)
        self.P1_ui.pushButton_P1_Edit_2.clicked.connect(self.CheckForSemesters)
        self.P1_ui.pushButton_P1_Del.clicked.connect(self.DeleteStudent)
        self.P1_ui.pushButton_P1_Info.clicked.connect(self.Show_P10)
        self.P1_ui.pushButton_P1_Info.clicked.connect(self.show_student_info)


        self.P2_ui.pushButton_P2_Add_2.clicked.connect(self.DeleteCourse)
        self.P2_ui.pushButton_P2_AddSem_2.clicked.connect(self.DeleteSemester)
        self.P2_ui.pushButton_P2_EditSem.clicked.connect(self.Show_P8)
        self.P2_ui.pushButton_P2_Add.clicked.connect(self.Show_P4)
        self.P2_ui.pushButton_P2_AddSem.clicked.connect(self.Show_P5)
        self.P2_ui.pushButton_2.clicked.connect(self.Show_P1)
        self.P2_ui.pushButton.clicked.connect(self.Show_P1)
        self.P2_ui.pushButton.clicked.connect(self.Add_Students)
        self.P2_ui.pushButton_P2_Edit.clicked.connect(self.Show_P7)
        
        
        self.P3_ui.pushButton_P3_Cancel.clicked.connect(self.Show_P1)
        self.P3_ui.pushButton_P3_Confirm.clicked.connect(self.Show_P1)
        self.P3_ui.pushButton_P3_Confirm.clicked.connect(self.EditStuInfo)
        self.P3_ui.pushButton_P3_E_Del.clicked.connect(self.Show_P7)
        self.P3_ui.pushButton_P3_E_Add.clicked.connect(self.Show_P4)
        self.P3_ui.pushButton_P3_E_AddSem.clicked.connect(self.Show_P5)
        self.P3_ui.pushButton_P3_E_EditCrs.clicked.connect(self.DeleteCourse)
        self.P3_ui.pushButton_P2_AddSem_2.clicked.connect(self.DeleteSemester)
        self.P3_ui.pushButton_P2_EditSem.clicked.connect(self.Show_P8)
        
        
        self.P4_ui.pushButton_P4_Cancel.clicked.connect(self.Show_Add_or_Edit)
        self.P4_ui.pushButton_P4_Add.clicked.connect(self.AddCourseToSem)
        self.P4_ui.pushButton_P4_Add.clicked.connect(self.UpdateTableCourses)
        self.P4_ui.pushButton_P4_Add.clicked.connect(self.Show_Add_or_Edit)
        
        
        self.P5_ui.pushButton_P5_Cancel.clicked.connect(self.Show_Add_or_Edit)   
        self.P5_ui.pushButton_P5_Add.clicked.connect(self.Add_Semesters)
        self.P5_ui.pushButton_P5_Add.clicked.connect(self.Show_Add_or_Edit)
        
        
        self.P7_ui.pushButton_P7_Confirm.clicked.connect(self.EditCourse)
        self.P7_ui.pushButton_P7_Confirm.clicked.connect(self.Show_Add_or_Edit)
        self.P7_ui.pushButton_P7_Cancel.clicked.connect(self.Show_Add_or_Edit)
        
        
        self.P8_ui.pushButton_P8_Confirm.clicked.connect(self.EditSemester)
        self.P8_ui.pushButton_P8_Confirm.clicked.connect(self.Show_Add_or_Edit)
        self.P8_ui.pushButton_P8_Cancel.clicked.connect(self.Show_Add_or_Edit)
        
        self.P10_ui.pushButton_P10_Print.clicked.connect(self.print_student_Info)
        self.P10_ui.pushButton_P10_back.clicked.connect(self.Show_P1)
        self.P10_ui.pushButton_P10_back.clicked.connect(self.Clear_Student_Info)

              
        
        
    #############################################
    ##### Code related to Page Transitions   ####
    #############################################      
    
    
    def Show_P1(self):
        self.layout.setCurrentIndex(0) 
        self.IsEditPage = False
        

        

        
    def Show_P2(self):
        self.layout.setCurrentIndex(1)
        self.CheckForStudentInfo()
        self.IsEditPage = False
        
        self.P2_ui.lineEdit.clear()
        self.P2_ui.lineEdit_2.clear()
        
    

        
    def Show_P3(self):
        self.layout.setCurrentIndex(2)
        self.IsEditPage = True
        
        self.P3_ui.lineEdit.clear()
        self.P3_ui.lineEdit_2.clear()
      
        
        
    def Show_P4(self):
        self.layout.setCurrentIndex(3)
            
    
        
    def Show_P5(self):
        self.layout.setCurrentIndex(4)
              
        
    def Show_P7(self):
        self.layout.setCurrentIndex(5)
           
        
    def Show_P8(self):
        self.layout.setCurrentIndex(6)
      

    def Show_P10(self):
        self.layout.setCurrentIndex(7)
       
          
                
    def Show_Add_or_Edit(self):
        
        if self.IsEditPage == True:
            self.layout.setCurrentIndex(2)
        
        if self.IsEditPage == False:
            self.layout.setCurrentIndex(1)
        
        self.P4_ui.lineEdit_P4_CCredit.clear()
        self.P4_ui.lineEdit_P4_CMarks.clear()  
        self.P4_ui.lineEdit_P4_CName.clear()  
        self.P4_ui.lineEdit_P4_CRef.clear()
        self.P4_ui.lineEdit_P4_CTitle.clear()   
        
        self.P5_ui.lineEdit_P5_SName.clear()    
      
      
    #############################################
    ############# Student Related Code  ########
    #############################################  
      
      
    # Adds All the main Attributes for a new student
       
    def Add_Students(self):
        
        self.name = self.P2_ui.lineEdit.text()
        self.ID = self.P2_ui.lineEdit_2.text()

        new_student = Stu(self.name, self.ID)

        self.Students_list.append(new_student)
        
        for i in self.NewStudentSems:
            new_student.addSemester(i)
        
             
        self.NewStudentSems.clear()  
        self.CheckForStudents()
    

        self.P2_ui.lineEdit.clear()
        self.P2_ui.lineEdit_2.clear()

       
        
        self.add_students_to_table()
          
          
          
          
          
    # Adds Students to the table in page 1 
         
    def add_students_to_table(self):
    
        widget = self.P1_ui.tableWidget_P1

        
        widget.setRowCount(0)
        
        self.P2_ui.tableWidget_P2.setRowCount(0)
        self.P2_ui.comboBox_P2.clear()
        self.P2_ui.comboBox_P2.addItem("--Semester")

       
        self.UpdateTableStudents()
                
          
          
          
    # gets the selected student's index from the table in page 1 
          
    def StudentIndex(self):
        
        self.StudentSelected = self.P1_ui.tableWidget_P1.selectedItems() 
        
        if self.StudentSelected:
         self.StuRowIndex = self.StudentSelected[0].row()
        
        
        
        
        
    # pops out the selected student from the list   
     
    def DeleteStudent(self):  
        
        self.Students_list.pop(self.StuRowIndex)
        
        widget = self.P1_ui.tableWidget_P1
        widget.setRowCount(0)
        
        
        self.UpdateTableStudents()
        self.CheckForStudents()
               
          
          
    # Makes sure the user has written a student name and ID for a new student
          
    def  CheckForStudentInfo(self):
    
        Wid_Name = self.P2_ui.lineEdit.text()
        
        Wid_ID = self.P2_ui.lineEdit_2.text()
        
        
        if len(Wid_Name.strip()) == 0 or len(Wid_ID.strip()) == 0:
            self.P2_ui.pushButton.setEnabled(False)
        
        if len(Wid_Name.strip()) != 0 and len(Wid_ID.strip()) != 0:
            self.P2_ui.pushButton.setEnabled(True)   
        
                  
    
    # Makes sure a student has been selected before editing or deleting
    
    def CheckForStudents(self):
        
          
        if self.isItemSelected_P1 == False :
            
            self.P1_ui.pushButton_P1_Del.setEnabled(False)
            
            self.P1_ui.pushButton_P1_Edit.setEnabled(False)
            
            self.P1_ui.pushButton_P1_Info.setEnabled(False)
            
            
        if  self.isItemSelected_P1 == True:
            
            self.P1_ui.pushButton_P1_Del.setEnabled(True)
            
            self.P1_ui.pushButton_P1_Edit.setEnabled(True)
            
            self.P1_ui.pushButton_P1_Info.setEnabled(True)
    
    
    
    
    # Setting a new Name and iD for an existing Student
    
    def EditStuInfo(self):
        
        self.NewName = self.P3_ui.lineEdit.text()
        
        self.NewID = self.P3_ui.lineEdit_2.text()
        
        if len(self.P3_ui.lineEdit.text()) != 0:
            
          self.SelectedStudent.setName(self.NewName)
         
        if len(self.P3_ui.lineEdit_2.text()) !=0:
            
          self.SelectedStudent.setID(self.NewID)
         
        self.UpdateTableStudents()  
        
        

    
    # Assigns the values of a student object to the table in Page 1, can be called repeatedly to update the table  
    
    def UpdateTableStudents(self):
        
      self.P1_ui.tableWidget_P1.setRowCount(0)
        
      self.Stutable = self.P1_ui.tableWidget_P1
        
      for student in self.Students_list:
        row_position = self.Stutable.rowCount()
        self.Stutable.insertRow(row_position)
        self.Stutable.setItem(row_position, 0, QTableWidgetItem(student.getName()))
        self.Stutable.setItem(row_position, 1, QTableWidgetItem(student.getID()))
        
          
    def Clear_Student_Info(self):
        
        
      self.P10_ui.comboBox_P10.clear()
      
      self.P10_ui.plainTextEdit.clear()
      
      self.P10_ui.comboBox_P10.setCurrentIndex(0)
      
      self.TextToPrint = ""
      
           
        
    
    def show_student_info(self):
        
        
        self.SelectedStudentIndex = self.StuRowIndex
        
        self.SelectedStudent = self.Students_list[self.SelectedStudentIndex]
        
        self.Details_Semesters = self.SelectedStudent.getSemesters().copy()
        
        self.P10_ui.comboBox_P10.addItem("Show All")
        
        for i in range(len(self.Details_Semesters)):
            self.P10_ui.comboBox_P10.addItem(self.Details_Semesters[i].GetSemName())
        
        
        
    def update_student_info(self):
        
        self.TextToPrint = ""
 
        if self.P10_ui.comboBox_P10.currentIndex() == 0:
            
            self.TextToPrint = self.SelectedStudent.__str__()
            
            self.P10_ui.plainTextEdit.setPlainText(self.TextToPrint)
            
          
        elif self.P10_ui.comboBox_P10.currentIndex() > 0:
            
            self.TextToPrint = str(self.Details_Semesters[self.P10_ui.comboBox_P10.currentIndex() - 1])
            
            self.P10_ui.plainTextEdit.setPlainText(self.TextToPrint)
        
           
    
        
        
           
    def print_student_Info(self):
        
        Printer = QPrinter()
        
        Widget = QApplication.instance().activeWindow()
        
        DocumentToPrint = QTextDocument()
        
        DocumentToPrint.setPlainText(self.TextToPrint)
        
        print_dialog = QPrintDialog(Printer, Widget)
        
        if print_dialog.exec_() == QPrintDialog.Accepted:
            
            DocumentToPrint.print_(Printer)
        
       
        
        
        
        
        
        
                
              


    #############################################
    ############# Course Related Code  ########
    #############################################  
    
    
    # Adds a course object to a selected semester object, contains the code for both Edit and Add pages
       
    def AddCourseToSem(self):
        
        
        if self.IsEditPage == True:
            
          self.CrsName = self.P4_ui.lineEdit_P4_CName.text()
          self.CrsTitle = self.P4_ui.lineEdit_P4_CTitle.text()
          self.CrsHrs = self.P4_ui.lineEdit_P4_CCredit.text()
          self.CrsRefNum = self.P4_ui.lineEdit_P4_CRef.text()
          self.CrsMark = self.P4_ui.lineEdit_P4_CMarks.text()
          
          if not str(self.CrsMark).isdigit()  :
              
              self.CrsMark = 0
              
          
          self.S[self.CBox_Index_P3].add_course(Crs(self.CrsName, self.CrsTitle, self.CrsRefNum, self.CrsHrs, 0, self.CrsMark))
          
          
         
        
        if self.IsEditPage == False :
        
          self.CBox_Index_P2 = self.P2_ui.comboBox_P2.currentIndex()
        
          self.CrsName = self.P4_ui.lineEdit_P4_CName.text()
          self.CrsTitle = self.P4_ui.lineEdit_P4_CTitle.text()
          self.CrsHrs = self.P4_ui.lineEdit_P4_CCredit.text()
          self.CrsRefNum = self.P4_ui.lineEdit_P4_CRef.text()
          self.CrsMark = self.P4_ui.lineEdit_P4_CMarks.text()
          
          if not str(self.CrsMark).isdigit() :
              
              self.CrsMark = 0
         
          self.NewStudentSems[self.CBox_Index_P2 - 1].add_course(Crs(self.CrsName, self.CrsTitle, self.CrsRefNum, self.CrsHrs, 0, self.CrsMark))
          
        self.P4_ui.lineEdit_P4_CName.clear()
        self.P4_ui.lineEdit_P4_CTitle.clear()
        self.P4_ui.lineEdit_P4_CCredit.clear()
        self.P4_ui.lineEdit_P4_CRef.clear()
        self.P4_ui.lineEdit_P4_CMarks.clear()
        self.CheckForCourses()  
        
     
     
    # gets the selected course's index from the table in page 2
     
    def CourseIndex_P2(self):
        
        self.CourseSelected_P2 = self.P2_ui.tableWidget_P2.selectedItems() 
        
        
        if self.CourseSelected_P2:
            
            self.CrsRowIndex_P2 = self.CourseSelected_P2[0].row()
            
          
          
    
    # Assigns new values for an existing course, contains code for both Edit and Add pages
          
    def EditCourse(self):
        
        if self.IsEditPage == False :
            
           self.SelectedSemesterCourses_P2 = self.NewStudentSems[self.CBox_Index_P2 - 1].get_courses()
           
           self.NewCrsName = self.P7_ui.lineEdit_P7_NewCName.text()
           self.NewCrsTitle = self.P7_ui.lineEdit_P7_NewCTitle.text()
           self.NewCrsHrs = self.P7_ui.lineEdit_P7_NewCCredit.text()
           self.NewCrsRefNum = self.P7_ui.lineEdit_P7_NewCRef.text()
           self.NewCrsMark = self.P7_ui.lineEdit_P7_NewCMarks.text()
           
           if not str(self.NewCrsMark).isdigit():
              
              self.NewCrsMark = 0
           
           
           
           if len(self.NewCrsName) != 0:
              self.SelectedSemesterCourses_P2[self.CrsRowIndex_P2].setName(self.NewCrsName)
              
           if len(self.NewCrsTitle) !=0:   
              self.SelectedSemesterCourses_P2[self.CrsRowIndex_P2].setTitle(self.NewCrsTitle)
           
           if len(self.NewCrsHrs) != 0:
              self.SelectedSemesterCourses_P2[self.CrsRowIndex_P2].setHours(self.NewCrsHrs)
              
           if len(self.NewCrsRefNum) != 0: 
              self.SelectedSemesterCourses_P2[self.CrsRowIndex_P2].setSubjectNumber(self.NewCrsRefNum)
              
           if len(str(self.NewCrsMark)) != 0 or isinstance(self.NewCrsMark, int):  
              self.SelectedSemesterCourses_P2[self.CrsRowIndex_P2].setMark(self.NewCrsMark)
              
           
           self.UpdateTableCourses()
           
        if self.IsEditPage == True:
            
            
           self.SelectedSemesterCourses_P3 = self.S[self.CBox_Index_P3].get_courses()
            
           self.NewCrsName = self.P7_ui.lineEdit_P7_NewCName.text()
           self.NewCrsTitle = self.P7_ui.lineEdit_P7_NewCTitle.text()
           self.NewCrsHrs = self.P7_ui.lineEdit_P7_NewCCredit.text()
           self.NewCrsRefNum = self.P7_ui.lineEdit_P7_NewCRef.text()
           self.NewCrsMark = self.P7_ui.lineEdit_P7_NewCMarks.text()
           
           
           if not str(self.NewCrsMark).isdigit():
              
              self.NewCrsMark = 0
           
           
           if len(self.NewCrsName) != 0:
              self.SelectedSemesterCourses_P3[self.CrsRowIndex_P3].setName(self.NewCrsName)
           
           if len(self.NewCrsTitle) !=0: 
              self.SelectedSemesterCourses_P3[self.CrsRowIndex_P3].setTitle(self.NewCrsTitle)
           
           if len(self.NewCrsHrs) != 0:
              self.SelectedSemesterCourses_P3[self.CrsRowIndex_P3].setHours(self.NewCrsHrs)
           
           if len(self.NewCrsRefNum) != 0:
              self.SelectedSemesterCourses_P3[self.CrsRowIndex_P3].setSubjectNumber(self.NewCrsRefNum)
           
           if len(str(self.NewCrsMark)) != 0 or isinstance(self.NewCrsMark, int):  
              self.SelectedSemesterCourses_P3[self.CrsRowIndex_P3].setMark(self.NewCrsMark)
           
           self.UpdateTableCourses()
           
        self.P7_ui.lineEdit_P7_NewCName.clear()
        self.P7_ui.lineEdit_P7_NewCTitle.clear()
        self.P7_ui.lineEdit_P7_NewCCredit.clear()
        self.P7_ui.lineEdit_P7_NewCRef.clear()
        self.P7_ui.lineEdit_P7_NewCMarks.clear()  
           
           
           
     
     
    # pops out a course from a selected semester's list of courses
    
    def DeleteCourse(self):  
        
        if self.IsEditPage == False:
        
            self.SelectedSemesterCourses_P2 = self.NewStudentSems[self.CBox_Index_P2 - 1].get_courses()
            
            self.SelectedSemesterCourses_P2.pop(self.CrsRowIndex_P2)
                
            widget = self.P2_ui.tableWidget_P2
            widget.setRowCount(0)
                
                
            
            
            
        if self.IsEditPage == True:
            
              self.SelectedSemesterCourses_P3 = self.S[self.CBox_Index_P3].get_courses()
       
              self.SelectedSemesterCourses_P3.pop(self.CrsRowIndex_P3)
                
              widget = self.P3_ui.tableWidget_P3
              widget.setRowCount(0)
                
                
                 
        
        self.CheckForCourses()
        self.UpdateTableCourses() 
        
     
     
     
     
     
    # Assigns the values of a course object to the tables in page 2 and 3, can be called repeatedly to update the tables 
    
    def UpdateTableCourses(self):
        
        if self.IsEditPage == True:
            
            
            self.S = self.SelectedStudentSems
            self.CBox_Index_P3 = self.P3_ui.comboBox_P3.currentIndex()
            self.P3_ui.tableWidget_P3.setRowCount(0)
            if len(self.S) != 0:
               for courses in self.S[self.CBox_Index_P3].get_courses():
                 row_position = self.P3_ui.tableWidget_P3.rowCount()
                 self.P3_ui.tableWidget_P3.insertRow(row_position)
                 
                 self.P3_ui.tableWidget_P3.setItem(row_position, 0, QTableWidgetItem(courses.getName()))
                 self.P3_ui.tableWidget_P3.setItem(row_position, 1, QTableWidgetItem(courses.getTitle()))
                 self.P3_ui.tableWidget_P3.setItem(row_position, 2, QTableWidgetItem(courses.getSubjectnumber()))
                 self.P3_ui.tableWidget_P3.setItem(row_position, 3, QTableWidgetItem(courses.getHours()))
                 self.P3_ui.tableWidget_P3.setItem(row_position, 4, QTableWidgetItem(str(courses.getMark())))
                 self.P3_ui.tableWidget_P3.setItem(row_position, 5, QTableWidgetItem(courses.getGrade()))
                
        
        
        
        
        if self.IsEditPage == False:
         self.CBox_Index_P2 = self.P2_ui.comboBox_P2.currentIndex()
        
         self.P2_ui.tableWidget_P2.setRowCount(0)
         if len(self.NewStudentSems) != 0:
          for courses in self.NewStudentSems[self.CBox_Index_P2 - 1].get_courses():
           row_position = self.P2_ui.tableWidget_P2.rowCount()
           self.P2_ui.tableWidget_P2.insertRow(row_position)
           
           self.P2_ui.tableWidget_P2.setItem(row_position, 0, QTableWidgetItem(courses.getName()))
           self.P2_ui.tableWidget_P2.setItem(row_position, 1, QTableWidgetItem(courses.getTitle()))
           self.P2_ui.tableWidget_P2.setItem(row_position, 2, QTableWidgetItem(courses.getSubjectnumber()))
           self.P2_ui.tableWidget_P2.setItem(row_position, 3, QTableWidgetItem(courses.getHours()))
           self.P2_ui.tableWidget_P2.setItem(row_position, 4, QTableWidgetItem(str(courses.getMark())))
           self.P2_ui.tableWidget_P2.setItem(row_position, 5, QTableWidgetItem(courses.getGrade()))
           
           
 

     
     
    # Makes sure an Item is selected from the table of courses to avoid errors 
     
    def CheckForCourses(self):
        
        if self.IsEditPage == True:
            
            if self.isItemSelected_P3 == False :
                
                self.P3_ui.pushButton_P3_E_Del.setEnabled(False)
                
                self.P3_ui.pushButton_P3_E_EditCrs.setEnabled(False)
            
            if  self.isItemSelected_P3 == True :
                
                self.P3_ui.pushButton_P3_E_Del.setEnabled(True)
                
                self.P3_ui.pushButton_P3_E_EditCrs.setEnabled(True)
            
            if len(self.S) == 0:
                
                self.P3_ui.pushButton_P3_E_Del.setEnabled(False)
                
                self.P3_ui.pushButton_P3_E_EditCrs.setEnabled(False)
        
                    

        if self.IsEditPage == False:
            
            self.CBox_Index_P2 = self.P2_ui.comboBox_P2.currentIndex()
            
            if len(self.NewStudentSems) != 0:
                
                if self.isItemSelected_P2 == False:
                    
                    self.P2_ui.pushButton_P2_Add_2.setEnabled(False)
                    
                    self.P2_ui.pushButton_P2_Edit.setEnabled(False)
                
                if  self.isItemSelected_P2 == True:
                    
                    self.P2_ui.pushButton_P2_Add_2.setEnabled(True)
                    
                    self.P2_ui.pushButton_P2_Edit.setEnabled(True) 
            
            if len(self.NewStudentSems) == 0 :
                
                self.P2_ui.pushButton_P2_Add_2.setEnabled(False)
                    
                self.P2_ui.pushButton_P2_Edit.setEnabled(False)
                  
                
    # gets the selected course's index from the table in page 3            
                     
    def CourseIndex_P3(self):
        
        self.CourseSelected_P3 = self.P3_ui.tableWidget_P3.selectedItems() 
        
        
        if self.CourseSelected_P3:
            
            self.CrsRowIndex_P3 = self.CourseSelected_P3[0].row()
              
     
     
     
    #############################################
    ############# Semester Related Code  ########
    #############################################  
    
      
     
    # Adds a new semester to a studnet, contains codes for both Add and Edit pages
    
    def Add_Semesters(self):
        
        
         if self.IsEditPage == False:
           
            self.name = self.P5_ui.lineEdit_P5_SName.text()

            self.NewSemester = Sem(self.name)
            
            self.NewStudentSems.append(self.NewSemester)
        
            self.P2_ui.comboBox_P2.addItem(self.name)
            
            self.P2_ui.comboBox_P2.setCurrentIndex(self.P2_ui.comboBox_P2.count() -1)
            
            self.P5_ui.lineEdit_P5_SName.clear()
            
            
            
         if self.IsEditPage == True:
             
            self.name = self.P5_ui.lineEdit_P5_SName.text()
            
            self.NewSemester = Sem(self.name)
            
            self.SelectedStudentSems.append(self.NewSemester)
            
            self.P3_ui.comboBox_P3.addItem(self.name)
            
            self.P3_ui.comboBox_P3.setCurrentIndex(self.P3_ui.comboBox_P3.count() -1)
            
            self.P5_ui.lineEdit_P5_SName.clear()
            
         self.CheckForSemesters()
            
            
        
        
        

    # pops out the selected semester
        
    def DeleteSemester(self):
        
        if self.IsEditPage == False:
            
            self.NewStudentSems.pop(self.CBox_Index_P2 - 1)
            
            self.SelectedSemester = self.P2_ui.comboBox_P2.currentIndex()
            
            self.P2_ui.comboBox_P2.removeItem(self.SelectedSemester)
            
        
        
        
        if self.IsEditPage == True:
            
           self.SelectedStudentSems.pop(self.CBox_Index_P3)
            
           self.SelectedSemester = self.P3_ui.comboBox_P3.currentIndex()
            
           self.P3_ui.comboBox_P3.removeItem(self.SelectedSemester)
            
        self.CheckForCourses()
        self.CheckForSemesters()
        
        
            
    # assigns a new name for a selected semester
            
    def EditSemester(self):
        
        
        if self.IsEditPage == True:
            
            self.CurrentlyEditingSem = self.SelectedStudentSems[self.CBox_Index_P3]
            
            self.NewSemName = self.P8_ui.lineEdit_P8_SName.text()
            
            self.P3_ui.comboBox_P3.setItemText(self.CBox_Index_P3, self.NewSemName)
            
            self.CurrentlyEditingSem.edit_semester_name(self.NewSemName)
            
            self.UpdateTableCourses()
            
            self.P8_ui.lineEdit_P8_SName.clear()
            
            
            
            
            
        if self.IsEditPage == False: 
            
            
            self.CurrentlyEditingSem = self.NewStudentSems[self.CBox_Index_P2 - 1]
            
            self.NewSemName = self.P8_ui.lineEdit_P8_SName.text()
            
            self.P2_ui.comboBox_P2.setItemText(self.CBox_Index_P2, self.NewSemName)
            
            self.CurrentlyEditingSem.edit_semester_name(self.NewSemName)
            
            self.UpdateTableCourses()
            
            self.P8_ui.lineEdit_P8_SName.clear()
        
        
       

            
            
            
    # makes sure a semester is selected before editing to avoid errors
            
    def CheckForSemesters(self):
               
                
        if self.IsEditPage == True:
            
            if len(self.S) == 0:
                
                self.P3_ui.pushButton_P2_EditSem.setEnabled(False)
                self.P3_ui.pushButton_P2_AddSem_2.setEnabled(False)
                self.P3_ui.pushButton_P3_E_Add.setEnabled(False)
                
            
            if len(self.S) != 0:
                
                self.P3_ui.pushButton_P2_EditSem.setEnabled(True)
                self.P3_ui.pushButton_P2_AddSem_2.setEnabled(True)
                self.P3_ui.pushButton_P3_E_Add.setEnabled(True)
                
  
        
                    

        if self.IsEditPage == False:
            
            if len(self.NewStudentSems) == 0:
                
                self.P2_ui.pushButton_P2_EditSem.setEnabled(False)
                self.P2_ui.pushButton_P2_AddSem_2.setEnabled(False)
                self.P2_ui.pushButton_P2_Add.setEnabled(False)
               
            
            if len(self.NewStudentSems) != 0:
                
                self.P2_ui.pushButton_P2_EditSem.setEnabled(True)
                self.P2_ui.pushButton_P2_AddSem_2.setEnabled(True)
                self.P2_ui.pushButton_P2_Add.setEnabled(True)
                
                
               
               
               
    
    
    #############################################
    ################ extra  Code  ###############
    #############################################              
               
               
               
               
                
    def CheckForSelectedItems_P1(self):
        
        self.IsItemSelectedRow_P1 = self.P1_ui.tableWidget_P1.selectedItems()
      
        
        if  len(self.IsItemSelectedRow_P1) == 0:
            self.isItemSelected_P1 = False
           
        
        if len(self.IsItemSelectedRow_P1) != 0:
            self.isItemSelected_P1 = True
        
        
        
        
        
        
    def CheckSelectedItems_P2(self):
        
        self.IsItemSelectedRow_P2 = self.P2_ui.tableWidget_P2.selectedItems()    
        
        if  len(self.IsItemSelectedRow_P2) == 0:
            self.isItemSelected_P2 = False
           
        
        if len(self.IsItemSelectedRow_P2) != 0:
            self.isItemSelected_P2 = True
        
        
        
        
        
                
    def CheckSelectedItems_P3(self):
        
        self.IsItemSelectedRow_P3 = self.P3_ui.tableWidget_P3.selectedItems()    
        
        if  len(self.IsItemSelectedRow_P3) == 0:
            self.isItemSelected_P3 = False
           
        
        if len(self.IsItemSelectedRow_P3) != 0:
            self.isItemSelected_P3 = True
        
        print(self.isItemSelected_P3)
        
            
          
    
    
    def EditPageOpened(self):
        
        
        self.P3_ui.comboBox_P3.clear()
        
        self.SelectedStudentIndex = self.StuRowIndex
        
        self.SelectedStudent = self.Students_list[self.SelectedStudentIndex]
       
    
        self.SelectedStudentSems = self.SelectedStudent.getSemesters()
        
     
        for i in self.SelectedStudentSems:
            self.P3_ui.comboBox_P3.addItem(str(i.GetSemName()))
            
            
        self.UpdateTableCourses()     
        
        
        
    def ClearLineEdits(self):
        
        self.P2_ui.lineEdit.clear()
        self.P2_ui.lineEdit_2.clear() 
        
        self.P3_ui.lineEdit.clear()  
        self.P3_ui.lineEdit_2.clear()
        
        self.P4_ui.lineEdit_P4_CCredit.clear()
        self.P4_ui.lineEdit_P4_CMarks.clear()  
        self.P4_ui.lineEdit_P4_CName.clear()  
        self.P4_ui.lineEdit_P4_CRef.clear()
        self.P4_ui.lineEdit_P4_CTitle.clear()   
        
        self.P5_ui.lineEdit_P5_SName.clear()
        
        self.P7_ui.lineEdit_P7_NewCCredit.clear()
        self.P7_ui.lineEdit_P7_NewCMarks.clear()  
        self.P7_ui.lineEdit_P7_NewCName.clear()  
        self.P7_ui.lineEdit_P7_NewCRef.clear()    
        self.P7_ui.lineEdit_P7_NewCTitle.clear() 
        
        self.P8_ui.lineEdit_P8_SName.clear() 

        
        
        
            
    
  
if __name__ == "__main__" :
    
    x = Main()
    x.starter()