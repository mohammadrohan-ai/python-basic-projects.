# Password Generator 🔐
# Generates random passwords based on user preferences.

import random
import string

print("Welcome to Password Generator!\n")
print("| PASSWORD GENERATOR |".center(50, "-"))
print("\n")

symbols = "!@#$%^&*()-_"
basic_pass = string.ascii_letters + string.digits
hard_pass = string.ascii_letters + string.digits + symbols

def password_generator():
    """
    Generates random passwords based on user-selected options.
    User can choose password length (1-15) and type (letters+digits or letters+digits+symbols).
    """
    while True:
        try:
            password_length = int(input("Enter the password length in integer (limit is 15): \n").strip())
            if password_length > 15 or password_length < 1:
                print("Your password is too long or too short.\n")
                continue

            password_type = int(
                input(
                    "Mode: letters+digits only (Enter 1), or letters+digits+symbols (Enter 2): \n"
                ).strip()
            )

            if password_type == 1:
                password = "".join(random.choices(basic_pass, k=password_length))
            elif password_type == 2:
                password = "".join(random.choices(hard_pass, k=password_length))
            else:
                print("Please enter a valid input (1 or 2).\n")
                continue

            print(f"\nHere's your password: {password}\n")

            while True:
                again = input("Do you want to generate another password? (yes/no): \n").lower().strip()
                if again in ("yes", "no"):
                    break
                else:
                    print("Please enter yes or no.\n")

            if again == "yes":
                continue
            else:
                print("Thank you for using our service! Have a nice day! 🌟\n")
                break

        except ValueError:
            print("Please enter a valid integer.\n")
            continue

if __name__ == "__main__":
    password_generator()
