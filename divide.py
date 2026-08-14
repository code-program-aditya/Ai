def divide_numbers():
    try:
        # Taking input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing division
        result = num1 / num2
        print(f"Result of division: {result:.2f}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")
    finally:
        print("Execution completed. Thank you for using the program.")


# Run the function
divide_numbers()
