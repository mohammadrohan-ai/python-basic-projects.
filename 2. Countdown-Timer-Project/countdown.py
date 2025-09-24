import time

def countdown():
    """
    Runs an interactive countdown timer.
    - Prompts the user for the number of seconds.
    - Counts down to zero, printing the time left each second.
    - Asks whether to run again after the timer ends.
    """
    while True:
        try:
            # Ask the user for countdown time in seconds
            seconds = int(input("Enter time for countdown (in seconds): ").strip())

            # Check for positive input
            if seconds <= 0:
                print("⚠️  Please enter a positive integer greater than 0.\n")
                continue

            # Countdown loop
            while seconds > 0:
                print(f"{seconds} seconds remaining")
                time.sleep(1)     # Wait 1 second
                seconds -= 1

            print("⏰ Time's Up!")

            # Ask if the user wants to start another countdown
            while True:
                again = input("Do you want to set a countdown again? (yes/no): ").strip().lower()
                if again in ("yes", "no"):
                    break
                else:
                    print("⚠️  Please type 'yes' or 'no'.\n")

            if again == "yes":
                # Loop back and start again
                continue
            else:
                print("✅ Okay, thanks for using the Countdown Timer!")
                break

        except ValueError:
            # Handles case where input is not a valid integer
            print("⚠️  Invalid input. Please enter a whole number.\n")
            continue


# Run the countdown only when the script is executed directly
if __name__ == "__main__":
    countdown()
