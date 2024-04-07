#wap to print the second largest and second smallest element in a list of a 10 integers without using sort function
def find_second_largest_smallest(arr):
    if len(arr) < 2:
        return "List should have at least 2 elements"

    # Initialize variables to store largest, second largest, smallest, and second smallest
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    # Iterate through the list
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_largest, second_smallest

# Take user input for the list of integers
numbers = []
print("Enter 10 integers:")
for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Call the function to find second largest and second smallest
second_largest, second_smallest = find_second_largest_smallest(numbers)
print("Second largest element:", second_largest)
print("Second smallest element:", second_smallest)