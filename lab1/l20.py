N = int(input("Enter the number of rows: "))

for i in range(1, N+1):
    print(" " * (N - i), end="")
    print("*" * (2*i - 1))

