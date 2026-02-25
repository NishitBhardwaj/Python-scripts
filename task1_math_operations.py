# Task 1: Perform Basic Mathematical Operations

def main():
    try:
        # Take input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        
        # Handle division separately to avoid division by zero
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Cannot divide by zero"

        # Display results
        print("\nResults:")
        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()