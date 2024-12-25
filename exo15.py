word = input("Please type in a string: ").lower()

vowels = ["a" ,"o","i"]
for x in vowels:
    if  x in word:
        print(f"{x} found")
    else:
        print(f"{x} not found")
        
