# I have one number 345 then sum of this num digit
user_input=int(input("Enter the 3 digit number:"))
q=user_input//100
print(q)
a=(user_input//10)%10
r=user_input%10
print(a)
print(r)
sum=q+a+r
print(f"The sum of Three digit is {sum}.")
