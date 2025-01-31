#Apply the Discount

import locale
unit = int(input("Enter number of units consumed: "))

def format_currency(amount):
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')  # Set locale for India (INR currency)
    return locale.currency(amount, grouping=True)
if unit <= 150:
    bill = unit * 2.40
elif unit > 150 and unit <= 300:
    bill = (150 * 2.40) + (unit - 150) * 3.00
else:
    bill = (150 * 2.40) + (150 * 3.00) + (unit - 300) * 3.20

print("Your bill is: ", bill)
rate1 = 2.40  #  first 150 units
rate2 = 3.00  # second 151-300 units
rate3 = 3.20  # third and  above 300 units
discount_rate = 0.10  # 10% discount for high consumption

if unit <= 150:
        bill = unit * rate1
elif unit > 150 and unit <= 300:
        bill = (150 * rate1) + (unit - 150) * rate2
else:
        bill = (150 * rate1) + (150 * rate2) + (unit - 300) * rate3
if unit >=500:
        discount = bill * discount_rate
        bill = discount
        print(f"Discount applied: {format_currency(discount)} (10% discount for over 500 units)")