def calculator():
    """
    A simple calculator program.

    Asks the user for two numbers and an operation, then prints the result.
    Includes error handling for invalid numbers, division by zero, and
    unsupported operations.
    """
    try:
        # Get input for the first number and convert it to a float
        num1 = float(input("Enter the first number: "))

        # Get input for the second number and convert it to a float
        num2 = float(input("Enter the second number: "))

        # Get input for the operation
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform calculation based on the operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
