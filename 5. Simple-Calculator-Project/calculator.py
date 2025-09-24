# Simple Calculator 🧮
# A console-based calculator that supports addition, subtraction, multiplication, and division.

def calculator():
    """
    Runs a simple calculator allowing users to perform addition, subtraction,
    multiplication, and division. Users can choose to continue or exit after each operation.
    """
    print("Welcome to the Calculator!\n")
    print("| CALCULATOR |".center(50, "-"))
    print("\n")

    while True:
        try:
            a = float(input("Enter your first number: ").strip())
            b = float(input("Enter your second number: ").strip())
            o = input("Enter operation (+, -, *, / or add, subtract, multiply, divide): ").strip().lower()

            if o in ("add", "+"):
                print(f"\nThe Addition of {a} and {b} is: {a + b}\n")
            elif o in ("subtract", "-"):
                print(f"\nThe Subtraction of {a} and {b} is: {a - b}\n")
            elif o in ("multiply", "*"):
                print(f"\nThe Multiplication of {a} and {b} is: {a * b}\n")
            elif o in ("divide", "/"):
                if b == 0:
                    print("\nCannot divide by zero.\n")
                else:
                    print(f"\nThe Division of {a} by {b} is: {a / b}\n")
            else:
                print("\nInvalid Input. Please try again.\n")
                continue

            while True:
                again = input("Do you want to use the calculator again? (yes/no): ").lower().strip()
                if again in ("yes", "no"):
                    break
                else:
                    print("Please enter yes or no.\n")

            if again == "yes":
                continue
            else:
                print("\nGoodbye! Thanks for using the Calculator. Have a nice day! 🌟\n")
                break

        except ValueError:
            print("\nInvalid input. Please enter valid numbers.\n")
            continue

if __name__ == "__main__":
    calculator()
