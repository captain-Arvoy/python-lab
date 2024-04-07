input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)
vowel_count = 0
consonant_count = 0
for char in input_string:
    if char in "AEIOUaeiou":
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)