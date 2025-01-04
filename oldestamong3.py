# User will input (3ages).Find the oldest one
age1=int(input("Enter The age of First Person:"))
age2=int(input("Enter The age of Second Person:"))
age3=int(input("Enter The age of Third Person:"))
if age1>=age2 and age1>=age3:
    print("Age 1 is the Oldest one.")
elif age2>=age3 and age2>=age1:
    print("Age 2 is the Oldest one.")
else:
    print("Age 3 is the Oldest one.")
