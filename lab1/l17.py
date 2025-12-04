N = int(input("Enter the value of N: "))

squares_dict = {}
for i in range(1, N+1):
    squares_dict[i] = i**2

print("Dictionary of squares:", squares_dict)

