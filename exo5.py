print("Runner 1:")
runner1_name = input("Name: ")
runner1_time = float(input("Time (in seconds): "))

print("Runner 2:")
runner2_name = input("Name: ")
runner2_time = float(input("Time (in seconds): "))

if runner1_time < runner2_time:
    print(f"The faster runner is {runner1_name}")
elif runner2_time < runner1_time:
    print(f"The faster runner is {runner2_name}")
else:
    print(f"{runner1_name} and {runner2_name} have the same time")