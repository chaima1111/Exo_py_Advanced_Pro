while True:
        n = int(input("Enter a positive integer N: "))
        
        if n > 0:
            for num in range(-n, n + 1):
                if num != 0:  # Exclude 0
                    print(num)
            break
        else:
            print("Please enter a positive integer.")

