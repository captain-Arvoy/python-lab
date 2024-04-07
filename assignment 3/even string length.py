string=input("enter a string : ")
words=string.split()
print("even-length words in the string:")
for word in words:
    if len(word)%2==0:
        print(word)