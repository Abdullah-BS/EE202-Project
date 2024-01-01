from Class_Semester import Semester, S1, S2
from Course import Course
from Course import C1, C2, C3, C4

class Student:
    def __init__(self, name='XXXXXX', ID='181810', semesters=None):
        self.name = name
        self.ID = ID
        if semesters is None:
            self.semesters = []
        else:
            self.semesters = semesters
    
    def setName(self, name):
        self.name = name
        
    def setID(self, ID):
        self.ID = ID
        
    def addSemester(self, semester):
        if isinstance(semester, Semester):
            self.semesters.append(semester)
    
    def getName(self):
        return self.name
    
    def getID(self):
        return self.ID
    
    def getSemesters(self):
          return self.semesters
      
  
    
    def getHours(self):
        hours = 0
        for semester in self.semesters:
            hours += semester.getHours()
        return hours
    
    def getPoints(self):
        points = 0
        for semester in self.semesters:
            points += semester.getPoints()
        return points
    
    def getGPA(self):
        if self.getHours() == 0 or self.getPoints() == 0:
            return 0
        return self.getPoints() / self.getHours()
    
    def __str__(self):
        
        info=f'Name: {self.name}\n'+ \
             f'ID: {self.ID}\n' + \
             f'GPA: {round(self.getGPA(), 2)}\n\n'
        
        for i in range(len(self.semesters)):
            info+=f"{self.semesters[i]}\n"
        return info
    
#=============================================================EXAMPLE=============================================================#

student1 = Student('Abdullah', 1111111, [S1, S2])
print(student1)