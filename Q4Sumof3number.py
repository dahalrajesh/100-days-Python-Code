#    Simple Sum of 3 number using oops im Python
class Sum_digit:
    def __init__(self):
        self.First_number=0
        self.Second_number = 0
        self.Third_number = 0

    def sum_num(self):
        self.First_number=int(input("Enter the First number:"))
        self.Second_number=int(input("Enter the Second_number:"))
        self.Third_number=int(input("Enter the Third_number:"))
        return self.First_number+self.Second_number+self.Third_number
#   create object and call the object then print the result
Sum=Sum_digit()
result=Sum.sum_num()
print(f"The sum of three number is{result}.")
