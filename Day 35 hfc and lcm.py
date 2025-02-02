# User will provide 2 numbers you have to find the HCF of those 2 numbers
# User will provide 2 numbers you have to find the by LCM of those 2 numbers
def find_hcf(a, b):
    factors_a = [i for i in range(1, a + 1) if a % i == 0]  # Find factors of 'a'
    factors_b = [i for i in range(1, b + 1) if b % i == 0]  # Find factors of 'b'

    common_factors = list(set(factors_a) & set(factors_b))  # Find common factors
    return max(common_factors)  # HCF is the largest common factor


# Get user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Compute HCF
hcf = find_hcf(a, b)

# Print result
print(f"HCF of {a} and {b} is: {hcf}")

#with using the math library function
import math
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
hcf=math.gcd(a,b)
print(hcf)
lcm=(a*b)//hcf
print(lcm)
