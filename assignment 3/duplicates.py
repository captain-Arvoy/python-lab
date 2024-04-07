def remove_duplicates(string):
    unique_chars = set()
    result = []

    for char in string:
        if char not in unique_chars:
            result.append(char)
            unique_chars.add(char)

    return ''.join(result)

string = input("Enter a string: ")
print(f"Original string: {string}")
print(f"String with duplicates removed: {remove_duplicates(string)}")