# 4. wap to enter a set and copy the content of the set into a new set one element at a time.
o_set=set(input('enter elements of the set separated by spaces:').split())
new_set=set()
for element in o_set:
    new_set.add(element)
print('new set after copying the content:')
print(new_set)