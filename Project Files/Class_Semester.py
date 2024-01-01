from Course import Course 
from Course import C1, C2, C3, C4
class Semester():
    
    def __init__(self,Semester_name, Courses = []):
        self.Semester_name=Semester_name
        self.Courses= list(Courses)
    
    def edit_semester_name(self,Semester_name):
        self.Semester_name=Semester_name
    
    def add_course(self,newCourses):
        self.Courses.append(newCourses)
    
    def get_courses(self):
        return self.Courses 
    
    def del_course(self,REcourse):
        self.Courses.remove(REcourse)
    
    def GetSemName(self):
        return self.Semester_name    

    def getPoints(self):
        points = 0
        for course in self.Courses:
            points += float(course.getPoints()) * float(course.getHours())
        return points
    
    def getHours(self):
        hours = 0
        for course in self.Courses:
            hours += float(course.getHours())
        return hours
    
    def getGPA(self):
        if self.getPoints() == 0 or self.getHours() == 0:
            return 0
        
        return round(self.getPoints()/self.getHours(), 2)
    
    def __str__(self):
        s = f"{self.Semester_name}\n" + \
            "----------------------------------------------------------------------------------------------\n\n"
        
        for i in range(len(self.Courses)):
            s+=str(self.Courses[i])+"\n"
        
        s += f'\nSemester GPA: {round(self.getGPA(), 2)}\t\t Hours: {self.getHours()}\t\t Points: {self.getPoints()}\n\n' +\
            "----------------------------------------------------------------------------------------------\n"
        return s
    
    
#=============================================================EXAMPLE=============================================================#

S1 = Semester('Fall-2024', [C1, C2])
# print(S1)

S2 = Semester('Winter-2024', [C3, C4])
# print(S2)