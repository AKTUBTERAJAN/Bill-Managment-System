#Calculate the Tax in rupees
unit = int(input("Enter number of units consumed: "))
rate1 = 2.40  #  first 150 units
rate2 = 3.00  # Second 151-300 units
rate3 = 3.20  # third and above above 300 units
tax_rate = 0.05  # 5% tax on the total bill
if unit <= 150:
        bill = unit * rate1
elif unit > 150 and unit <= 300:
        bill = (150 * rate1) + (unit - 150) * rate2
else:
        bill = (150 * rate1) + (150 * rate2) + (unit - 300) * rate3
tax = bill * tax_rate
bill += tax
print(f"Total Tax of Consumed {unit} unit is: {tax:.2f} Rupees, Include (5% tax)")