import math
r = float(input("Enter radius of base (in cm): "))
h = float(input("Enter height of cylinder (in cm): "))
# Calculate the volume of the cylinder
volume = math.pi * (r**2) * h
# Convert volume to liters (1 liter = 1000 cubic centimeters)
litre = volume / 1000
cost = 40 * litre
# Print the results
print("Volume of the cylinder is {:.2f} cm³".format(volume))
print("Volume in liters: {:.2f} L".format(litre))
print("Cost of milk: Rs {:.2f}".format(cost))
