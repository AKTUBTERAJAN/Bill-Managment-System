#Display bill in details for breack down
unit = int(input("Enter number of units consumed: "))
       
def calculate_bill(unit):
    # Define rate
    rate1 = 2.40  #  first 150 units
    rate2 = 3.00  # second 151-300 units
    rate3 = 3.20  # third above 300 units
    

    # Bill calculation
    if unit <= 150:
        bill = unit * rate1
    elif unit > 150 and unit <= 300:
        bill = (150 * rate1) + (unit - 150) * rate2
    else:
        bill = (150 * rate1) + (150 * rate2) + (unit - 300) * rate3
    # Return final bill
    return bill
def main():
    # Input validation
    while True:
        try:
            
            if unit < 0:
                print("Please enter a valid positive number of units.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate and print the bill
    final_bill = calculate_bill(unit)

    # Display detailed breakdown
    print("\nDetailed Breakdown:")
    if unit <= 150:
        print(f"Units at {2.40}/unit: {unit} units")
    elif unit > 150 and unit <= 300:
        print(f"Units at {2.40}/unit: 150 units")
        print(f"Units at {3.00}/unit: {unit - 150} units")
    else:
        print(f"Units at {2.40}/unit: 150 units")
        print(f"Units at {3.00}/unit: 150 units")
        print(f"Units at {3.20}/unit: {unit - 300} units")

    print(f"\nTotal Bill: ₹{final_bill:.2f}")

# Run the program
main()