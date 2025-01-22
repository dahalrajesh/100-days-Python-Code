# User will input (2numbers).Write a program to swap the numbers

import time
# I will take the input from the user first num and second num two input:

first_number=int(input("Enter the first number:"))
time.sleep(2)
second_number=int(input("Enter the Second number:"))

# I want to hold here for 4 second :
print(f"First Number is {first_number} and second number is {second_number}  before swap.")
time.sleep(4)
# Simple Swap logic:
temp=first_number
first_number=second_number
second_number=temp
print(f"First Number is {first_number} and second number is {second_number}  after swap.")
