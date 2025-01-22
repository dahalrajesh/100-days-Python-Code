# Write a program that take a user input of three angles and will find out whether it can form a triangle
# to make a triangle it sum must be equal to 180

# user wil give three input and I have to check whether 3 input sum is 180 or not
while True:
    X=int(input('Enter the First Degree:'))
    Y=int(input('Enter the Second Degree:'))
    Z=int(input('Enter the Third Degree:'))
    Sum=X+Y+Z
    if Sum == 180 and X>0 and Y>0 and Z>0:
        print("The Given is triangle.")
    else:
        print("The given is not Triangle")
    user_input=input(print("Do you want to continue (Yes/No)"))
    if user_input!="Yes":
        break
