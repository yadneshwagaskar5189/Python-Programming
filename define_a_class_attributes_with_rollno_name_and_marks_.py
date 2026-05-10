class Student:
    def __init__(self,rollno,name,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("Roll no:-",self.rollno)
        print("Name:-",self.name)
        print("Marks:-",self.marks)
s1=Student(10,"Priyanshu",99)
s1.display()