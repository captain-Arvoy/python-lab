#wap to create two lists first list containing 5 integers and second list containing 5 strings,print both the lists one element from each list combined at a time
n = [1, 2, 3, 4, 5]
strings = ['apple', 'banana', 'orange', 'grape', 'kiwi']
for num, string in zip(n, strings):
    print(num,string)