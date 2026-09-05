"""
Author: Daniel Aragão

Background: You work for a retail store that wants to increase sales on Tuesday and Wednesday,
which are the store's slowest sales days. On Tuesday and Wednesday,
if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%
"""
from datetime import datetime

today = datetime.now()
dow = today.weekday()

discount_rate = .1
tax_rate = .06
discount = 0
price = 1
quantity = 1
subtotal = 0
while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: "))
        subtotal += price * quantity

print()
subtotal = round(subtotal, 2)
print(f"Subtotal ${subtotal:.2f}")
if (dow == 1 or dow == 2) and subtotal >= 50:
    discount = subtotal * discount_rate
    subtotal -= discount

    tax = subtotal * tax_rate
    total = subtotal + tax

    print(f"Discount ${discount:.2f}")
    print(f"Tax ${tax:.2f}")
    print(f"Total due ${total:.2f}")
elif (dow == 1 or dow == 2) and (subtotal < 50 and subtotal !=0):
    print(f"Buy more ${(50 - subtotal):.2f} worth of products to receive a 10% discount! ")

else:
    tax = subtotal * tax_rate
    total = subtotal + tax

    print(f"Tax ${tax:.2f}")
    print(f"Total due ${total:.2f}")

