# Employee class that can exist independently
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee: {self.name}, ID: {self.emp_id}"

# Department class that aggregates Employee(s)
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # List to store Employee references

    def add_employee(self, employee):
        self.employees.append(employee)  # Aggregation: reference to existing Employee

    def show_employees(self):
        print(f"Department: {self.dept_name}")
        for emp in self.employees:
            print(emp.get_details())

# Example usage:
emp1 = Employee("Rameen", 1011)
emp2 = Employee("Abeeha", 1012)

# Create department and add employees
dept = Department("Computer Science")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()
