# Student Registration System

## EE-202 Project


## Table of Contents

- [Introduction](#introduction)
- [Class Structure](#class-structure)
  - [Class Course](#class-course)
  - [Class Semester](#class-semester)
  - [Class Student](#class-student)
- [Main File](#main-file)

---

## Introduction

This ReadMe file contains a brief explanation of the **"Student Registration System"** functionality. It explains and displays information about the class structures used in this project, with UML diagrams for each class. At the end of this document, the main file, which includes the full project with the GUI pages, will be briefly explained.

## Class Structure

### Class Course

The first class in this project is about the courses that the students take. This class consists of several methods, which are shown in the figures below, along with the UML diagram.

- The constructor method (Figure 1) requires six arguments to create an object from the `Course` class.
- Each argument has a `GET` method to print the attribute and a `SET` method to change the value of the attribute (Figures 2-4).
- The `__str__` method for the class is shown in Figure 5.

The UML Diagram for the `Course` class is shown in Table 1.

![Figure 1: Constructor Method](![Figure 1: Constructor Method](![image](https://github.com/Abdullah-BS/EE202-Project/assets/139412761/c8f3a8dc-19d2-455c-9acf-f16f5ec84b61))
![Figure 2: GET Method](![Uploading image.png…]()
)
![Figure 3: SET Method](path/to/figure3.png)
![Figure 4: Additional Methods](path/to/figure4.png)
![Figure 5: __str__ Method](path/to/figure5.png)

### Class Semester

The second class in this project deals with semesters, which will have objects of the `Course` class and will be added to objects of the `Student` class. The UML diagram for the `Semester` class is shown alongside its attributes.

- The constructor method (Figure 6) requires two arguments: the name of the semester and the objects of the `Course` class added to the list of an object of the `Semester` class.
- Each attribute has a `GET` and `SET` method (Figures 6-7).
- Methods to remove, add, or get courses in the `Semester` class are also provided.
- The `__str__` method for this class is shown in Figure 8.

The UML Diagram for the `Semester` class is shown in Table 2.

![Figure 6: Constructor Method](path/to/figure6.png)
![Figure 7: GET and SET Methods](path/to/figure7.png)
![Figure 8: __str__ Method](path/to/figure8.png)

### Class Student

The `Student` class is the final class to complete this project. It contains objects from both the `Semester` and `Course` classes and will be added to a list in the main file to be used as data.

- The constructor method (Figure 9) requires three arguments: the full name of the student, the ID number, and a `Semester` object, which will be added to a list in the `Student` object.
- Each attribute has a `GET` and `SET` method (Figures 9-10).
- Methods to control the `Semester` objects include adding a semester to the list, getting the list of semesters, and removing a semester from the list.
- The `__str__` method for the `Student` class is shown in Figure 11.

The UML Diagram for the `Student` class is shown in Table 3.

![Figure 9: Constructor Method](path/to/figure9.png)
![Figure 10: GET and SET Methods](path/to/figure10.png)
![Figure 11: __str__ Method](path/to/figure11.png)

## Main File

The main file contains all the classes mentioned above and all the GUI pages, which are displayed below. Combining all the work into one file helps us modify or add GUI pages without the risk of starting from scratch. The main file has many lines of code. For example, connecting buttons on each GUI page to functions that either show information or execute commands, among other purposes. Due to the large amount of code, the full file cannot be shown here, but the diagram will explain the GUI structure in a simpler way, which replaces the need to show the code. The code is briefly explained in Figure 12 below, and GUI pages are shown in Figures 13-
