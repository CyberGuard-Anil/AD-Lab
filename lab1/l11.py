
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            # Swap the numbers
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list in ascending order:", numbers)

