try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print(f"Result is: {result}")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("You can’t divide by zero.")
