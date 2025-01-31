
import datetime
import re
import locale
import sys

# Function to format currency
def format_currency(amount):
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')  # Set locale for India (INR currency)
    return locale.currency(amount, grouping=True)

# Function to calculate the electricity bill
def calculate_bill(unit):
    # Define rate
    rate1 = 2.40  # first 150 units
    rate2 = 3.00  # second 151-300 units
    rate3 = 3.20  # after last 300 units
    discount_rate = 0.10  # 10% discount for high consumption
    tax_rate = 0.05  # 5% tax on the total bill

    # Bill calculation
    if unit <= 150:
        bill = unit * rate1
    elif unit > 150 and unit <= 300:
        bill = (150 * rate1) + (unit - 150) * rate2
    else:
        bill = (150 * rate1) + (150 * rate2) + (unit - 300) * rate3

    # Apply discount for high consumption
    if unit > 500:
        discount = bill * discount_rate
        bill -= discount
        print(f"Discount applied: {format_currency(discount)} (10% discount for over 500 units)")

    # Add tax
    tax = bill * tax_rate
    bill += tax
    print(f"Tax applied: {format_currency(tax)} (5% tax)")

    # Return final bill
    return bill

# Function to validate user input
def get_valid_unit_input():
    while True:
        user_input = input("Enter number of units consumed: ")
        if re.match(r"^\d+$", user_input):  # Check if input is a positive integer
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid positive integer.")

# Function to modify the bill
def modify_bill(bill):
    print("Modify the bill options:")
    print("1. Change the number of units")
    print("2. Modify rates (discount/tax)")
    print("3. Exit modification")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        unit = get_valid_unit_input()
        bill = calculate_bill(unit)
    elif choice == "2":
        print("Modifying discount or tax is not yet supported in this version.")
    elif choice == "3":
        print("Exiting modification.")
    else:
        print("Invalid choice. Exiting modification.")
    
    return bill

# Function to delete the bill
def delete_bill():
    print("Bill deleted successfully!")
    return None

# Main function to run the program
def main():
    # Print current date and time (using datetime module)
    print(f"Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Initial bill calculation
        unit = get_valid_unit_input()
        final_bill = calculate_bill(unit)

        # Display the final bill in formatted currency
        print(f"\nTotal Bill: {format_currency(final_bill)}")
        
        # Give the user options to edit, delete, or modify the bill
        while True:
            print("\nChoose an option:")
            print("1. Edit the bill (change number of units)")
            print("2. Delete the bill")
            print("3. Exit")
            option = input("Enter your choice (1/2/3): ")
            
            if option == "1":
                final_bill = modify_bill(final_bill)
                if final_bill is None:
                    break
            elif option == "2":
                final_bill = delete_bill()
                if final_bill is None:
                    break
            elif option == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose again.")
        
        # If the bill is deleted, the program will exit
        if final_bill is not None:
            print(f"\nFinal Bill: {format_currency(final_bill)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)  # Exit the program in case of error

# Run the program
if __name__ == "__main__":
    main()