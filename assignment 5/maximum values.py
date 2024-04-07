# 2.wap to create a dictionary and print the key which has the maximum value
my_dict = {'a': 10, 'b': 20, 'c': 15, 'd': 5}
max_key = max(my_dict, key=my_dict.get)
print("Key with maximum value:", max_key)
