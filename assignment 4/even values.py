# wap to create a function that takes a list as argument and the returns the even value of the list. print the new list with even values
def get_even_values(input_list):
    return [x for x in input_list if x % 2 == 0]
# Input from user
input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
even_values = get_even_values(input_list)
print("List with even values:", even_values)
