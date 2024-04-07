# 3.wap to print the transpose of a matrix of m*n order

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(m)]
transpose = [list(row) for row in zip(*matrix)]
for row in transpose:
    print(row)
