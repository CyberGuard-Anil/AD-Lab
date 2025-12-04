class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary: {self.salary}")

    def annual_salary(self):
        return self.salary * 12


name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))

emp = Employee(name, salary)
emp.display_details()
print(f"Annual Salary: {emp.annual_salary()}")

