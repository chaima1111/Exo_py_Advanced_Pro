def length(lst):
    count = 0
    for ls in lst:
        count += 1
    return count


def mean(lst):
    if length(lst) == 0:  #  division by zero error
        return 0
    total = 0
    for num in lst:
        total += num
    return total / length(lst)

def range_of_list(lst):
    if length(lst) == 0:
        return 0
    else:
         max_val = lst[0]
    min_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val - min_val
numbers = [1, 2, 3, 4, 5]
empty = []
neg = [-2,-4,-5,-6]
fl = [12.3,14.5,18.9]
print("Length",length(numbers) ,end=" ")
print(f"Mean :{mean(numbers)}",end=" ")
print(f"Range :{range_of_list(numbers)}")
# empty
print("----empty---")
print("Length",length(empty) ,end=" ")
print(f"Mean :{mean(empty)}",end=" ")
print(f"Range :{range_of_list(empty)}")
print("----negative values---")
print("Length",length(neg) ,end=" ")
print(f"Mean :{mean(neg)}",end=" ")
print(f"Range :{range_of_list(neg)}")
print("----float values---")
print("Length",length(fl) ,end=" ")
print(f"Mean :{mean(fl):.2f}",end=" ")
print(f"Range :{range_of_list(fl):.2f}")
