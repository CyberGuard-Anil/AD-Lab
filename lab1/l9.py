numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("List of numbers:", numbers)
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))

