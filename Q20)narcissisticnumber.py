# Program to check if a 4-digit number is a narcissistic number
n = int(input("Enter a 4-digit number: "))

# Check if the input is a 4-digit number
if 1000 <= n <= 9999:
    # Calculate the sum of each digit raised to the power of 4
    sum_of_powers = sum(int(digit) ** 4 for digit in str(n))
    
    # Check if the number is equal to the sum of its digits raised to the power of 4
    if n == sum_of_powers:
        print(f"{n} is a narcissistic number.")
    else:
        print(f"{n} is not a narcissistic number.")
else:
    print("Please enter a valid 4-digit number.")
