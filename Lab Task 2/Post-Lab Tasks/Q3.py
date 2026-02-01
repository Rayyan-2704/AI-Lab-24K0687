class Student:
    def __init__(self, name, student_id, marks = 0):
        self.name = name
        self.student_id = student_id
        self.__marks = marks
    
    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            print(f"Error: Please enter marks between 0 to 100 inclusive!")
        else:
            self.__marks = marks
    
    def get_marks(self):
        return self.__marks
    
    def calculate_grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 50:
            return "D"
        else:
            return "Fail"
        
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Marks: {self.__marks}/100")
        print(f"Grade: {self.calculate_grade()}")

def main():
    s1 = Student("Rayyan Aamir", "CS-1003", 92)
    s2 = Student("Usman Hasan", "CS-1005", 45)
    s3 = Student("Hammad Haider", "CS-1009", 68)

    print(f"------------ Printing Details of Student 1 ------------")
    s1.display_details()

    print(f"\n------------ Printing Details of Student 2 ------------")
    s2.display_details()

    print(f"\n------------ Printing Details of Student 3 ------------")
    s3.display_details()

main()