# Student Registration System

## EE-202 Project


## Table of Contents

- [Introduction](#introduction)
- [Class Structure](#class-structure)
  - [Class Course](#class-course)
  - [Class Semester](#class-semester)
  - [Class Student](#class-student)
- [Main File](#main-file)
- [Conclusion](#conclusion)

---

## Introduction

This Page contains a brief explanation of the **"Student Registration System"** functionality. It explains and displays information about the class structures used in this project, with UML diagrams for each class. At the end, the main file, which includes the full project with the GUI pages, will be briefly explained.

## Class Structure

### Class Course

The first class in this project is about the courses that the students take. This class consists of several methods, which are shown below, along with the UML diagram.

- The constructor method `__init__` requires six arguments to create an object from the `Course` class.
- Each argument has a `get` method to print the attribute and a `set` method to change the value of the attribute.

```
class Course:
    def __init__(self, name = "",  title="", subjectNumber= 0, hours= 0, section=0 , mark=int(0)):
        self.title = title
        self.name = name
        self.subjectNumber = str(subjectNumber)
        self.hours = hours
        self.section = section
        self.mark = int(mark)
        self.info=[title, subjectNumber, hours, section, mark]
    
    def setTitle(self, newTitle):
        self.title = newTitle
    
    def setName(self, newName):
        self.name = newName  
    
    def setSubjectNumber(self, newSubjectNumber):
        self.subjectNumber = newSubjectNumber

    def setHours(self, newHours):
        self.hours = newHours
    
    def setSection(self, newSection):
        self.section = newSection
    
    def setMark(self, newMark):
        self.mark = int(newMark)
    
    def setGrade(self, newgrade):
        self.grade = int(newgrade)
        
    def getName(self):
        return self.name    
    
    def getTitle(self):
        return self.title

    def getSubjectnumber(self):
        return self.subjectNumber
    
    def getHours(self):
        return self.hours
    
    def getSection(self):
        return self.section
    
    def getMark(self):
        return str(self.mark)
    
    def getGrade(self):
        if self.mark >= 95:
            self.grade = 'A+'

        elif self.mark >= 90:
            self.grade = 'A'

        elif self.mark >= 85:
            self.grade = 'B+'
            
        elif self.mark >= 80:
            self.grade = 'B'

        elif self.mark >= 75:
            self.grade = 'C+'

        elif self.mark >= 70:
            self.grade = 'C'

        elif self.mark >= 65:
            self.grade = 'D+'

        elif self.mark >= 60:
            self.grade = 'D'

        else:
            self.grade = 'F'

        return self.grade
    
    def getPoints(self):
        if self.mark >= 95:
            self.points = 5.0

        elif self.mark >= 90:
            self.points = 4.75

        elif self.mark >= 85:
            self.points = 4.5
            
        elif self.mark >= 80:
            self.points = 4.0

        elif self.mark >= 75:
            self.points = 3.5

        elif self.mark >= 70:
            self.points = 3.0

        elif self.mark >= 65:
            self.points = 2.5

        elif self.mark >= 60:
            self.points = 2.0

        else:
            self.points = 1.0

        return self.points
    def getCourse(self):
        return self.info     
    
    def __str__(self):
        s = f'{self.subjectNumber}' + (10-len(self.subjectNumber))*' ' + \
            f' {self.title}' + (35-len(self.title))*' ' + \
            f' {self.name}' + (35-len(self.name))*' ' + \
            f' {self.hours}' + (10-len(str(self.hours)))*' ' + \
            f' {self.section}' + (10-len(str(self.section)))*' ' + \
            f' {self.mark}' + (10-len(str(self.mark)))*' ' + \
            f' {self.getGrade()}' + (10-len(str(self.getGrade())))*' ' + \
            f' {self.getPoints()}'
        
        return s
```

### The UML Diagram for the class `Course:`


![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/60835744-8b50-48f5-8c87-a43b6b9df69c)


---


### Class Semester

The second class in this project deals with semesters, which will have objects of the `Course` class and will be added to objects of the `Student` class. The UML diagram for the `Semester` class is shown alongside its attributes.

- The constructor method requires two arguments: the name of the semester and the objects of the `Course` class added to the list of an object of the `Semester` class.
- Each attribute has a `get` and `set` method.
- Methods to remove, add, or get courses in the `Semester` class are also provided.

```
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
```


### The UML Diagram for the `Semester` class:

![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/e787a700-7c2c-4984-b6de-c8693b97b2bb)

---


### Class Student

The `Student` class is the final class to complete this project. It contains objects from both the `Semester` and `Course` classes and will be added to a list in the main file to be used as data.

- The constructor method requires three arguments: the full name of the student, the ID number, and a `Semester` object, which will be added to a list in the `Student` object.
- Each attribute has a `get` and `set` method.
- Methods to control the `Semester` objects include adding a semester to the list, getting the list of semesters, and removing a semester from the list.

```
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
```


### The UML Diagram for the `Student` class:

![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/9409c735-922c-4c0f-a0fa-5a4aa6617e15)

---


## Main File

The main file contains all the classes mentioned above and all the GUI pages, which are displayed below. Combining all the work into one file helps us modify or add GUI pages without the risk of starting from scratch. The main file has many lines of code. For example, connecting buttons on each GUI page to functions that either show information or execute commands, among other purposes. Due to the large amount of code, the full file cannot be shown here, but the diagram will explain the GUI structure in a simpler way, which replaces the need to show the code.

### GUI Structure:
![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/7dccb01a-057f-4aba-9e4f-37356f06dfec)

---


### GUI Pages:

![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/00dcdca3-6b31-4b5c-89ec-99db88dedd9f)


![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/8ed96380-fde2-4b71-80c2-3835d183fcbc)


![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/305768c9-dfa5-49b5-abe3-7b805e8b2632)


![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/d45f1f01-1424-4d5b-bed4-ada1fbcc0561)


![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/2d9b6da0-fab2-4f39-96e1-f63f7e95b13b)


![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/62845555-42f6-48ad-bf55-4d63cd234a5f)



---
## Conclusion
To conclude, this project has provided invaluable experience in applying concepts learned in the EE-202 course. Through the implementation of the Student Registration System, we have deepened our understanding of class structures, object-oriented programming, and graphical user interface design. Moreover, the project has honed our skills in problem-solving, teamwork, and self-learning, which are essential attributes for success in the field of programming and engineering. We look forward to building upon this experience in future projects and endeavors.
