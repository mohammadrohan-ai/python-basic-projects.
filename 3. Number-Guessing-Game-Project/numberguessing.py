# Number Guessing Game
# The computer picks a random number, and the user tries to guess it with hints (high/low).

import random

LOW, HIGH = 1, 100

def game():
    """
    Runs the number guessing game. The computer selects a random number between LOW and HIGH.
    The user is prompted to guess until they find the correct number.
    After each round, the user can choose to play again.
    """
    print("Welcome to the Number Guessing Game!")
    print(f"The number will be between {LOW} and {HIGH}.\n")

    while True:  # outer loop: entire game session
        random_number = random.randint(LOW, HIGH)
        attempts = 0

        while True:  # inner loop: guesses for one round
            attempts += 1
            try:
                guess = int(input(f"Guess a number between {LOW} and {HIGH}: ").strip())
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            if guess < LOW or guess > HIGH:
                print(f"Out of range! Please guess a number between {LOW} and {HIGH}.\n")
            elif guess > random_number:
                print("Too high! Try again.\n")
            elif guess < random_number:
                print("Too low! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempt(s). "
                      f"The number was {random_number}.\n")
                again = input("Do you want to play again? (yes/no): ").strip().lower()
                if again != "yes":
                    print("Thanks for playing! Goodbye!")
                    return
                else:
                    print("\nStarting a new round!\n")
                    break  # start a new round

if __name__ == "__main__":
    start = input("Do you want to play the game? (yes/no): ").strip().lower()
    if start == "yes":
        game()
    else:
        print("Okay, maybe next time! Have a great day!")
