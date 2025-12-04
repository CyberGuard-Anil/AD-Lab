numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

if numbers[0] > numbers[1]:
    first = numbers[0]
    second = numbers[1]
else:
    first = numbers[1]
    second = numbers[0]

for i in range(2, len(numbers)):
    if numbers[i] > first:
        second = first
        first = numbers[i]
    elif numbers[i] > second:
        second = numbers[i]

print("The second largest number is:", second)

