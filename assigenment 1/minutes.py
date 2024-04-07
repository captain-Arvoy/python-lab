minutes=int(input("Enter time in minutes: "))
hours=minutes // 60
remaining_minutes=minutes % 60
print("Minutes is equal to hours: ", hours)
print("Remaining minutes: ",remaining_minutes)
print("Total time = ", hours,remaining_minutes)