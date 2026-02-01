class Employee:
    def __init__(self, name, emp_id):
        self._name = name
        self._emp_id = emp_id

    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"Employee Name: {self._name}")
        print(f"Employee ID: {self._emp_id}")
    
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary
    
    def display_details(self):
        super().display_details()
        print(f"Employee Type: Full-Time Employee")
        print(f"Monthly Salary: ${self._monthly_salary:.2f}")

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate

    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate
    
    def display_details(self):
        super().display_details()
        print(f"Employee Type: Part-Time Employee")
        print(f"Hours Worked: {self._hours_worked}")
        print(f"Hourly Rate: ${self._hourly_rate:.2f}")

def main():
    f1 = FullTimeEmployee("Rayyan Aamir", "F-1005", 75350)
    p1 = PartTimeEmployee("Usman Hasan", "P-3009", 36, 24.87)

    print(f"------------ Printing Details of Full-Time Employee ------------")
    f1.display_details()
    print(f"Overall Salary: ${f1.calculate_salary():.2f}")

    print(f"\n------------ Printing Details of Part-Time Employee ------------")
    p1.display_details()
    print(f"Overall Salary: ${p1.calculate_salary():.2f}")    

main()