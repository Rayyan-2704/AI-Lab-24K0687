def main():
    students = {}
    for i in range(3):
        name = input("Enter student name: ").strip()
        marks = int(input("Enter marks: "))
        students[name] = marks

    print("\nStudent Records:")
    for name, marks in students.items():
        print(f"{name}: {marks}")

if __name__ == "__main__":
    main()