# 2.wap to print a matrix along with summation of row elements and column elements after entering a 3*3 matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)
matrix = []
print("Enter the elements of the 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)
print("Matrix:")
print_matrix(matrix)

print("Sum of row elements:")
for i in range(3):
    row_sum = sum(matrix[i])
    print(f"Row {i+1}: {row_sum}")
print("Sum of column elements:")
for j in range(3):
    col_sum = sum(row[j] for row in matrix)
    print(f"Column {j+1}: {col_sum}")
