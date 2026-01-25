def main():
    name = input("Enter student name: ").strip()
    marks = int(input("Enter marks: "))

    if marks >= 85:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Student Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()