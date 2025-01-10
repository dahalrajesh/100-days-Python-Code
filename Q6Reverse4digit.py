# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
try:
    user_input = int(input("Enter the 4 digit Number:"))
    if 1000<=user_input<=9999:
        thousand=user_input//1000
        hundred=(user_input//100)%10
        ten=(user_input//10)%10
        one=user_input%10
        reversed = one * 1000 + ten * 100 + hundred * 10 + thousand
        print(f"The Reversed Number is {reversed}")

        if user_input == reversed:
            print("The reversed number is the same as the original (Palindrome).")
        else:
            print("The reversed number is different from the original.")
    else:
        print("Invalid number. Please enter a 4-digit number.")
except ValueError:
    print("Invalid input. Please enter integers only.")
