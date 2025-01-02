numbers =[]
runnning = True
while runnning:
    value = input("enter an value: ")
    if value.lstrip("-").isdigit():
        value = int(value)
        if not value ==0:
            numbers.append(value) 
            print(f"Current List: {numbers}",end=" ")
            numbers.sort()
            print(f"Sorted List : {numbers}" )
        else:
            runnning=False
            