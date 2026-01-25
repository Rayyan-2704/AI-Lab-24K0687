def main():
    n = int(input("Enter a number: "))
    count = 0

    print("Even numbers: ", end = "")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end = " ")
            count = count + 1

    print(f"\nTotal even numbers: {count}")

if __name__ == "__main__":
    main()