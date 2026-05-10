class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        print("Constructor is called for",self.name)

    def display(self):
        print("Employee ID:",self.emp_id)
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
        
    def __del__(self):
        print("Destructor is called for",self.name)

e1=Employee(101534,"Sarthak",50000)
e1.display()
del e1                
