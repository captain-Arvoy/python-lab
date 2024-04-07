# wap to create a function that prints the first n numbers of the fibonacci series without using recursion
def fibonacci(n):
    if n <= 0:
        return []

    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])

    return fib_series[:n]

# Input from user
n = int(input("Enter the number of Fibonacci numbers to print: "))
fib_series = fibonacci(n)
print("Fibonacci series:", fib_series)
