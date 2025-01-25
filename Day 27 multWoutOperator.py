# Write a program that can multiply 2 numbers provided by the user without using the * operator

num1=int(input("Enter the first num1:"))
num2=int(input("Enter the Second num2:"))

result=0
abs_num2=abs(num2)
for i in range(abs_num2):
    result+=num1

if abs_num2<0:
    result=-result
print(result)
