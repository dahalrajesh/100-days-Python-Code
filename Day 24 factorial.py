# Write a program that can find the factorial of a given number provided by the user.

number=int(input("Enter the number for get the factorial of the given number:"))
fact=1
for i in range(1,number+1):
    fact=fact*i
print(f"The factorial of {number} is {fact}")
