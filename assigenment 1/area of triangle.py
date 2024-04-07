a = int(input("enter an integer:"))
b = int(input("enter an integer:"))
c= int(input("enter an integer:"))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is ',area)