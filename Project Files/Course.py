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
    
#=============================================================EXAMPLE=============================================================#

C1= Course("EE-202","Object_Orianted_Programing", 11222, 4, 22331, 98)
# print(C1)
C2= Course("Basic","EE-250",11225, 4, 32424, 85)
# print(C2)
C3= Course("Math","Math=204", 11555, 6, 98552, 80)
C4= Course("IE","IE-201",55555, 5, 11515, 100)
# print(C1)