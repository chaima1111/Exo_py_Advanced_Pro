
while True:
    width = int(input("enter a width : "))
    height = int(input("enter a height : "))
    if width >=0 and height >=0:
        break
    else:
        continue
for j in range (0,height):
    for i in range(0,width):
        print("#",end="")
    print(" ",end=" ")