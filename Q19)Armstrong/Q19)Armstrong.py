# Write a program that will check whether the number is armstrong number or not.
while True:
    try:
        n=int(input("Enter the number:"))

        length_of_digit=len(str(n))
        # print(length_of_digit)
        sum_of_digit=sum(int(digit)**length_of_digit for digit in str(n))
        print(sum_of_digit)
        if sum_of_digit==n:
            print("The given number is Armstrong.")
        else:
            print("It is not armstrong.")
    except:
        print("You have enter the wrong input pleaase enter the valid input.")
    user_input=input("Do you want to continue the further more(yes/no)")
    if user_input!="yes":
            break

