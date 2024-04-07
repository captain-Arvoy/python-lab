# Program to Check Leap Year
year=int(input("Enter year to be checked:"))
if(year%100 !=0)or(year%400==0 and year%4==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")