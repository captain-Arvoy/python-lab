#wap to create an integer list of 20 elements increase the odd value element by 5
num=list(range(1,21))
num=[i+5 if i%2!=0 else i for i in num]
print("modified list with odd values increased by 5")
print(num)