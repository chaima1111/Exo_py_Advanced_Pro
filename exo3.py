
total_amount = float(input("Total amount: "))
number_of_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ").strip().capitalize()


if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount = 0.10  
elif day_of_week in ["Saturday", "Sunday"]:
    discount = 0.20  
else:
    print("Invalid day of the week entered.")
    exit()  

discounted_price = total_amount * (1 - discount)

if number_of_items > 5:
    discounted_price *= 0.95

print(f"Total price after discount: {discounted_price:.1f} dinars")
