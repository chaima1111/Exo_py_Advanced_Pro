numbers = [1, 2, 3, 4, 5]
is_running=True
while is_running :
    index = input("enter an index (-1 to quit): ")
    if index.lstrip("-").isdigit() :
        index =int(index)
        
        if index != -1:
            if(index<=4):
                value = input("enter an value: ")
                if value.isdigit():
                    value = int(value)
                    numbers.insert(index ,value) 
                    print(numbers)
            else:
                print("out of range")
        else:
                is_running = False
    else:
        print("enter an integer value!")



