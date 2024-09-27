class Employee:
    def _init_(self, name, salary, performance_rating):
        self.name = name
        self.salary = salary
        self.performance_rating = performance_rating

class HRSystem:
    def _init_(self):
        self.employees = {}

    def create_employee(self, name, salary, performance_rating):
        self.employees[name] = Employee(name, salary, performance_rating)

    def read_employee(self, name):
        return self.employees.get(name)

    def update_employee(self, name, salary=None, performance_rating=None):
        employee = self.employees.get(name)
        if employee:
            if salary:
                employee.salary = salary
            if performance_rating:
                employee.performance_rating = performance_rating

    def delete_employee(self, name):
        if name in self.employees:
            del self.employees[name]

    def calculate_salary(self, name):
        employee = self.read_employee(name)
        if employee:
            return employee.salary

    def generate_performance_report(self, name):
        employee = self.read_employee(name)
        if employee:
            return f"Employee Name: {employee.name}\nPerformance Rating: {employee.performance_rating}"

hr_system = HRSystem()

while True:
    print("1. Create Employee")
    print("2. Read Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Calculate Salary")
    print("6. Generate Performance Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        performance_rating = float(input("Enter performance rating: "))
        hr_system.create_employee(name, salary, performance_rating)
        print(f"employee '{name}' created successfully.")
    elif choice == "2":
        name = input("Enter employee name: ")
        employee = hr_system.read_employee(name)
        if employee:
            print(f"Name: {employee.name}, Salary: {employee.salary}, Performance Rating: {employee.performance_rating}")
    elif choice == "3":
        name = input("Enter employee name: ")
        salary = float(input("Enter new salary (0 to keep current): "))
        performance_rating = float(input("Enter new performance rating (0 to keep current): "))
        hr_system.update_employee(name, salary if salary != 0 else None, performance_rating if performance_rating != 0 else None)
    elif choice == "4":
        name = input("Enter employee name: ")
        hr_system.delete_employee(name)
    elif choice == "5":
        name = input("Enter employee name: ")
        print(f"Salary: {hr_system.calculate_salary(name)}")
    elif choice == "6":
        name = input("Enter employee name: ")
        print(hr_system.generate_performance_report(name))
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
