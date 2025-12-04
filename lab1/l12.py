text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special_chars = 0

vowel_letters = "aeiouAEIOU"

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        if char in vowel_letters:
            vowels += 1
        else:
            consonants += 1
    else:
        special_chars += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special_chars)

