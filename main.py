import random
from datetime import datetime, timedelta

print("Hello, welcome to the coffee shop")
name = input("May I have your name? ")

print("Welcome " + name + " to our shop!")

menu = 'black coffee, espresso, latte, cappuccino'

print("Here is our menu: " + menu + " The prices are as follows:\n")
print("Black coffee: $3\nEspresso: $5\nLatte: $7\nCappuccino: $8\n")

total = 0
description = ""

ordering = True

while ordering:
    order = input("\nWhat would you like to order?\nSelect \n 1 for black coffee\n 2 for espresso\n 3 for latte\n 4 for cappuccino:\n")

    if order == "1":
        print("You have ordered black coffee. Do you want to add milk for an extra $2?")
        milk = input("Yes or no: ")
        if milk.lower() == "yes":
            total += 5
            description += "Black coffee with milk\n"
        else:
            total += 3
            description += "Black coffee\n"

    elif order == "2":
        print("You have ordered espresso. Do you want to add extra sugar for an extra $1?")
        sugar = input("Yes or no: ")
        if sugar.lower() == "yes":
            total += 6
            description += "Espresso with extra sugar\n"
        else:
            total += 5
            description += "Espresso\n"

    elif order == "3":
        print("You have ordered latte. Do you want to add extra sugar for an extra $1?")
        sugar = input("Yes or no: ")
        if sugar.lower() == "yes":
            total += 8
            description += "Latte with extra sugar\n"
        else:
            total += 7
            description += "Latte\n"

    elif order == "4":
        print("You have ordered cappuccino. Choose a size:")
        size = input("Large (extra $4), Medium (extra $2), or Regular (no extra charge): ").lower()
        if size == "large":
            total += 12
        elif size == "medium":
            total += 10
        else:
            total += 8
        description += f"Cappuccino ({size})\n"

    else:
        print("Sorry, we don't have that on the menu.")

    another = input("Would you like to order something else? (yes/no): ")
    if another.lower() != "yes":
        ordering = False

# Delivery or Pickup Option
method = input("\nWould you like:\n 1 for Delivery\n 2 for Pickup\nSelect: ")

# Get current datetime
now = datetime.now()
prep_minutes = random.randint(5, 10)
prep_time = now + timedelta(minutes=prep_minutes)

if method == "2":
    print(f"\nOrder Summary for {name}:")
    print(f"- Items:\n{description.strip()}")
    print(f"- Total: ${total}")
    print(f"- Order placed at: {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"- Estimated pickup time: {prep_time.strftime('%H:%M')}")
    print("\nThank you! Your order will be ready soon.")

elif method == "1":
    delivery_minutes = random.randint(15, 30)
    delivery_time = prep_time + timedelta(minutes=delivery_minutes)
    print(f"\nOrder Summary for {name}:")
    print(f"- Items:\n{description.strip()}")
    print(f"- Total: ${total}")
    print(f"- Order placed at: {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"- Estimated time to prepare: {prep_minutes} minutes")
    print(f"- Estimated delivery arrival: {delivery_time.strftime('%H:%M')}")
    print("\nThank you! Your order will be delivered soon.")

else:
    print("Invalid selection for delivery or pickup.")
