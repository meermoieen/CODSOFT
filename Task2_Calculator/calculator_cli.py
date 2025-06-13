def calculator():
    print("🧮 Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")

        choice = input("Enter your choice (+, -, *, /): ")

        if choice == '+':
            result = num1 + num2
        elif choice == '-':
            result = num1 - num2
        elif choice == '*':
            result = num1 * num2
        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("❌ Cannot divide by zero.")
                return
        else:
            print("❌ Invalid operation.")
            return

        print(f"\n✅ Result: {num1} {choice} {num2} = {result}")

    except ValueError:
        print("❌ Please enter valid numbers.")

calculator()
