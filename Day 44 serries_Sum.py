import math

def series_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i / math.factorial(i)
    return total_sum

# Take user input
n = int(input("Enter the value of n: "))
result = series_sum(n)
print(f"The sum of the series up to {n} terms is: {result}")
