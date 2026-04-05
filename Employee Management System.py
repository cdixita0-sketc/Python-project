print("--- Python OOP Project: Employee Management System ---")
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person created with name: {name} and age: {age}.")

    def display(self):
        print("\nPerson Details:")
        print("Name:",self.name)
        print("Age:",self.age)

class Employee(Person):
    def __init__(self,emp_id,name,age,salary):
        super().__init__(name,age)
        self.__emp_id = emp_id
        self.__salary = salary
        print(f"Employee created with name: {name}, age:{age}, ID: {emp_id}, and salary: {salary}")

    def get_emp_id(self):
        return self.__emp_id
    
    def set_emp_id(self,emp_id):
        if id > 0:
            self.__emp_id = emp_id
        else:
            print("Invalid id")
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def __del__(self):
        pass

    def display(self):
        super().display()
        print("\nEmployee Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee_id:",self.get_emp_id())
        print("Salary:",self.get_salary())

class Manager(Employee):
    def __init__(self,name,age,emp_id,salary,department):
        super().__init__(emp_id,name,age,salary)
        self.department = department
        print(f"Manager created with name: {name} age:{age}, ID: {emp_id}, salary: {salary}, and department:{department}")

    def display(self):
        super().display()
        print("\nManager Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee_ID:",self.get_emp_id())
        print("Salary:",self.get_salary())
        print("Department:",self.department)

class Developer(Employee):
    def __init__(self,name,age,emp_id,salary,programming_language):
        super().__init__(emp_id,name,age,salary,)
        self.programming_language = programming_language
        print(f"Developer created with name:{name}, age:{age},ID:{emp_id}, salary:{salary}, and  {programming_language}")

    def display(self):
        super().display()
        print("\nDeveloper Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee_Id:",self.get_emp_id())
        print("Salary:",self.get_salary())
        print("Programming_language:",self.programming_language)

person = None
employee = None
manager = None
devloper = None

while True:
    print("\nchoose an operation:")
    print("1. Create a person")
    print("2. create an Employee")
    print("3. Create a manager")
    print("4. Create a Devloper")
    print("5. show Details")
    print("6. Exit")

    choise = int(input("Enter your choise:"))

    if choise == 1:
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        person = Person(name,age)
        print("\n--- Choose another operation ---")

    elif choise == 2:
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        emp_id = input("Enter Employee ID:")
        salary = int(input("Enter Salary:"))
        employee = Employee(emp_id,name,age,salary)

    elif choise == 3:
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        emp_id = input("Enter Employee ID:")
        salary = int(input("Enter Salary:"))
        department = input("Enter Department:")
        manager = Manager(name,age,emp_id,salary,department)

    elif choise == 4:
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        emp_id = input("Enter Employee ID:")
        salary = int(input("Enter Salary:"))
        programming_language = input("Enter Programming Language:")
        devloper = Developer(name,age,emp_id,salary,programming_language)

    elif choise == 5:
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")
        d = int(input("Enter your choise:"))

        if d == 1:
            person.display()
        elif d == 2:
            employee.display()
        elif d == 3:
            manager.display()
        elif d == 4:
            devloper.display()
        else:
            print("Data not available.")

    elif choise == 6:
        print("\nExiting the system.All reources have been freed.")
        print("\nGoodbye!")
        break

    else:
        print("Invalid choise!")
    



           
    

    