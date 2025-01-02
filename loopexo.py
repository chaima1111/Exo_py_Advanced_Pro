while True:
    value = input("enter positive integer :")
    if value.isdigit():
        value = int(value)
        if value>=0:
            for i in range (1,value+1):
                for j in range (1,value+1):
                    print (f"{i}*{j} = {i*j}")
            break
    else:
        print("enter a positive integer ")


