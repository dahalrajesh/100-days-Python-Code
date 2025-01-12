# Write a program that will check whether the number is armstrong number or not.
def is_armstrong_number(number):
    # Convert the number to a string to extract its digits
    digits = list(map(int, str(number)))
    num_digits = len(digits)

    # Calculate the sum of the digits raised to the power of num_digits
    armstrong_sum = sum(digit ** num_digits for digit in digits)

    # Check if the calculated sum is equal to the original number
    return armstrong_sum == number


user_input = int(input("Enter a number to check if it is an Armstrong number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
