# Write a program that will take three digits from the user and add the square of each digit.

a=int(input("Enter the number of 3 Digits:"))
hundred=(a//100)
ten=(a%100)//10
one=a%10
Square=hundred**2+ten**2+one**2

# print(Square)
print("The sum of the squares of the digits is:", Square)
