
people = int(input("How many people need a ride? "))
taxi_capacity = int(input("How many people fit in one taxi? "))

full_taxis = people // taxi_capacity  
if people % taxi_capacity != 0: 
    full_taxis += 1

print(f"Number of taxis needed: {full_taxis}")
