# Write a program to find the sum of first n numbers,
# where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def find_sum():
    n=int(input("Enter the number you want to get the sum of:"))
    sum=n*(n+1)//2
    print(f"The  Sum of teh given number is {sum} ")
find_sum()
