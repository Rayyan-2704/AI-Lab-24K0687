def main():
    while True:
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 + num2
                print(f"Result: {result}")

            case 2:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 - num2
                print(f"Result: {result}")

            case 3:
                print("Exiting...")
                break

            case _:
                print("Invalid choice!")

    print("Goodbye!")

if __name__ == "__main__":
    main()