# 3.wap to enter a dictionary and remove the duplicate value inside the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 3, 'd': 3}
new_values = {}
for key, value in my_dict.items():
    if value not in new_values.values():
        new_values[key] = value
print("Original Dictionary:", my_dict)
print("Dictionary with Unique Values:", new_values)
