"""class Student:
    def __init__(self, name, rollno):
        self.name = name         #instance variable
        self.rollno = rollno     #instance variable

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollno)


s1 = Student("Prashant", 100)
s2 = Student("Amit:",101 )

s1.display()
s2.display()"""

class Student:
    def __init__(self, name, rollno):
        self.name = name   #instance variable
        self.rollno = rollno     #instance variable

    def display(self):           #local variable
        greeting = "Hello"

        print(greeting, self.name, "-", self.rollno)

s1 = Student("Prashant", 101)
s1.display()
