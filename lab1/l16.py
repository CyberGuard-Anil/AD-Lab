names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")  

print("\nNames in the file:")
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  

