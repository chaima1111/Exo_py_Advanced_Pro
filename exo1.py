
name = input("Please enter your name: ").strip()


if name.lower() == "vip":
    print("Enjoy the show for free!")
else:
    
    try:
        tickets = int(input("How many tickets would you like to buy? "))
        if tickets <= 0:
            print("Please enter a valid number of tickets greater than zero.")
        else:
            ticket_price = 15.50
            total_cost = tickets * ticket_price


            print(f"The total cost for {tickets} ticket(s) is ${total_cost:.2f}")
            print(f"Thank you, {name}. Enjoy your tickets!")
    except ValueError:
        print("Invalid input! Please enter a whole number for the tickets.")
