numbers=[]
shoe_sizes=[]

for i in range(1,6):
    numbers.append(i)

for i in range(8,13):
    shoe_sizes.append(i)

third =numbers + shoe_sizes
print(f" Numbers List: {numbers} Shoe Sizes List: {shoe_sizes}")
print(f"the combined list {third}")