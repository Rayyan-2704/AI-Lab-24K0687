def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def main():
    n = int(input("Enter the number of marks: "))
    marks = []

    for i in range(n):
        mark = int(input(f"Enter marks {i + 1}: "))
        marks.append(mark)

    print(f"\nMarks: {marks}")
    print(f"Average Marks: {calculate_average(marks):.1f}")

if __name__ == "__main__":
    main()