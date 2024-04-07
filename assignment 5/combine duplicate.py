# 6. wap to enter two different sets with string elements combine both the sets remove any duplicates are present, print the new set
set1 = eval(input("Enter the first set: "))
set2 = eval(input("Enter the second set: "))
new_set = set1 | set2
print("Combined set with duplicates removed:",new_set)