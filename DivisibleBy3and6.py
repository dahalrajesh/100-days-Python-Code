# Function to check divisibility
def is_divisible_by_3_and_6(number):
    if number % 3 == 0 and number % 6 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_divisible_by_3_and_6(number):
    print(f"The number {number} is divisible by both 3 and 6.")
else:
    print(f"The number {number} is NOT divisible by both 3 and 6.")
