while True:
    print("=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter Your Choice (1-5): "))

    if choice == 5:
        print("Goodbye!")
        break

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == 1:
            print("The Sum Is:", num1 + num2)

        elif choice == 2:
            print("The Difference Is:", num1 - num2)

        elif choice == 3:
            print("The Product Is:", num1 * num2)

        elif choice == 4:
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print("The Quotient Is:", num1 / num2)

    else:
        print("Invalid Choice")
