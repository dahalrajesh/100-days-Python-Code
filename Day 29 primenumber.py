# Get user input for a number between 100 and 999
n = int(input("Enter the number in Range 100 to 999: "))

# Check if the number is within the range of 100 to 999
if 100 <= n <= 999:
    # Extract hundreds, tens, and ones digits
    hundred = n // 100
    tens = (n % 100) // 10
    one = n % 10

    # Calculate the Armstrong number by cubing the digits and summing them
    armstrng = hundred**3 + tens**3 + one**3

    # Check if the number is an Armstrong number
    if armstrng == n:
        print(f"The given number {n} is an Armstrong number.")
    else:
        print(f"The given number {n} is not an Armstrong number.")
else:
    print("Please enter a number in the range of 100 to 999.")
