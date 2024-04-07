num = input("Enter a 5-digit number: ")

if len(num) == 5 and num.isdigit():
    d1, d3, d5 = num[0], num[2], num[4]
    print(f"At odd positions: {d1}, {d3}, {d5}")
else:
    print("Invalid input. Please enter a 5-digit number.")
