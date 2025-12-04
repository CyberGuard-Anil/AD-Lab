
list1 = input("Enter elements of first list separated by space: ").split()

list2 = input("Enter elements of second list separated by space: ").split()

common_elements = []
for element in list1:
    if element in list2 and element not in common_elements:
        common_elements.append(element)

print("Elements present in both lists:", common_elements)

