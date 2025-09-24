# Simple Shopping Bill Calculator

def billing():
    """
        A simple shopping bill calculator.
        Continuously asks the user for item prices until '0' is entered.
        Prints a receipt with all items and the total bill.
        """
    total = 0           # running total of all item prices
    prices = []         # list to store prices of individual items
    while True:
        try:
            user_input = float(input("Enter the price of item or enter '0' to quit: \n").strip())

            # If user wants to quit, break out of the loop
            if user_input == 0:
                break
            elif user_input < 0:
                print("Please enter a number greater than 0.\n")
                continue
            else:
                price = user_input
                prices.append(price)          # add this item to the list
                total += price                # update running total
                print(f"Current total: {total}$")
        except ValueError:
            # Handles case where input is not valid.
            print("Please enter a valid number or '0' to quit.")

# --- After the loop ends, print the final receipt ---
    print("\n--- Receipt ---")
    for index, price in enumerate(prices, start=1):
        print(f"Item {index}: {price}$")
    print(f"Total bill: {total}$")
    print("Thank you for shopping!")

# Run the program only when this file is executed directly

if __name__ == "__main__":
    billing()
