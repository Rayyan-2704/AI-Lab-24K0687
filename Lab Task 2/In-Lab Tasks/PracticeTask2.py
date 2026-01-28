class Staff:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")

class Teacher(Staff):
    def __init__(self, name, staff_id, department, courses, salary):
        super().__init__(name, staff_id, department)
        self.courses = courses
        self.salary = salary
        
    def teach_course(self):
        print(f"{self.name} is teaching the following courses: {self.courses}")
        
    def display_info(self):
        super().display_info()
        print(f"Courses: {self.courses}")
        print(f"Salary: ${self.salary:.2f}")

class Admin(Staff):
    def __init__(self, name, staff_id, department, role, working_hours):
        super().__init__(name, staff_id, department)
        self.role = role
        self.working_hours = working_hours
        
    def perform_task(self):
        print(f"{self.name} is performing the administrative tasks of {self.role}.")
        
    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")
        print(f"Working Hours: {self.working_hours}")

class ResearchAssistant(Staff):
    def __init__(self, name, staff_id, department, research_topic, stipend):
        super().__init__(name, staff_id, department)
        self.research_topic = research_topic
        self.stipend = stipend
        
    def working_on_research(self):
        print(f"{self.name} is working on a research related to {self.research_topic}.")
        
    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")
        print(f"Stipend: ${self.stipend:.2f}")

def main():
    teacher = Teacher("Dr. Farrukh Salim", "T-1001", "Computer Science", ["AI", "Discrete Structures", "Operating Systems"], 3200.50)
    admin = Admin("Tariq Rasheed", "A-2004", "Admissions", "Admin Head", 14)
    researcher = ResearchAssistant("Rayyan Aamir", "R-3005", "Computer Science", "Deep Learning", 1250.25)
    
    print("--------- Teacher Information ---------")
    teacher.display_info()
    teacher.teach_course()
    
    print("\n--------- Admin Information ---------")
    admin.display_info()
    admin.perform_task()
    
    print("\n--------- Research Assistant Information ---------")
    researcher.display_info()
    researcher.working_on_research()

main()