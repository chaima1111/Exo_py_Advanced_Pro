
import json
from datetime import datetime
import os

ARRAY_FILE = "array.json"

def save_act(act):
    with open(ARRAY_FILE, 'w') as f:
        json.dump(act, f, indent=4)
def load_list():
    if os.path.exists(ARRAY_FILE):
        with open(ARRAY_FILE, 'r') as f:
            return json.load(f)
    return {}
act=[]
numbers = [1, 2, 3, 4, 5]
menu = ["Append","Insert","Pop","Remove","Sort","Reverse","Quit"]
for i in range(0,len(menu)):
    print(f"{i+1}.{menu[i]}")
    
runnning = True
while runnning:
    option = input(f"enter a option between 1 and {len(menu)} :")
    if option.isdigit() :
        option =int(option)
        if option <=len(menu)+1 and option >0:
            if option ==1 :
                value = input("enter an value: ")
                if value.lstrip("-").isdigit():
                    value = int(value)
                    numbers.append(value) 
                    print(numbers)
            elif option ==2:
                value = input("enter an value: ")
                if value.lstrip("-").isdigit():
                    value = int(value)
                    index = input("enter an index : ")
                    if index.isdigit() :
                        index =int(index)
                        if(index<=len(numbers)):
                                numbers.insert(index ,value) 
                                print(numbers)
                        else:
                            print("out of range")
                    else:
                        print("the index must be an integer ")
                        
            elif option == 3:
                numbers.pop()
                print(numbers)
            elif option == 4:
                index = input("enter an index : ")
                if index.isdigit() :
                    index =int(index)
                    if(index<=len(numbers)):
                            numbers.remove(index ) 
                            print(numbers)
                    else:
                        print("out of range")
                else:
                    print("index must be an integer")
            elif option ==5:
                numbers.sort()
                print(numbers)
            elif option==6:
                numbers.reverse()
                print(numbers)
            elif option ==7:
                runnning = False
                print("Thank you!")
        
            test_result = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "option": option,
            "list": numbers,
            }
            act.append(test_result)
            save_act(act)
        
        else:
            print("the option must be between 1 and 5")

lists = load_list()
print("---------------your modification-------")
for lis in lists:
    if not lis["option"] ==7:
        print(f"{lis["option"]} : {lis["list"]}")
