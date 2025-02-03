def fibonacci(n):
    fib_series = [0, 1]  # Starting values
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])  # Add the last two numbers
    return fib_series

# Print the first 20 Fibonacci numbers
print(fibonacci(20))
