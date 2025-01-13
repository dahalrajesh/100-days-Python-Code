# Input: Principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))
# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")
