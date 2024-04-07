x=int(input("Enter value of x: "))
s=0
for i in range(1,x):
    if x%i==0:
        s+=i

if s==x:
    print("It's a perfect number.")
else:
    print("It's not a perfect number.")