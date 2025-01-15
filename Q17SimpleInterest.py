# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
class SimpleInterest:

    def __init__(self):
        self.principal = 0
        self.rate = 0
        self.time_period = 0

    def calculation(self):
        self.principal = float(input("Enter the principal amount: "))
        self.rate = float(input("Enter the rate of interest: "))
        self.time_period = float(input("Enter the time period (in years): "))
        return (self.principal * self.rate * self.time_period) / 100
si = SimpleInterest()
simple_interest = si.calculation()
print(f"The simple interest is: {simple_interest:.2f}.")
