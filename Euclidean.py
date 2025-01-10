# Write a program to find the euclidean distance between two coordinates.
from fontTools.misc.cython import returns

# X1=int(input("Write the value of X1:"))
# X2=int(input("Write the value of X2:"))
# Y1=int(input("Write the value of Y1:"))
# Y2=int(input("Write the value of Y2:"))
# # Power is Given By **
#
# ED=((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
#
# print(f"The value of ED is {ED}")

##
class  Euclidean:
    def num(self):
        self.X1 = int(input("Write the value of X1:"))
        self.X2 = int(input("Write the value of X2:"))
        self.Y1 = int(input("Write the value of Y1:"))
        self.Y2 = int(input("Write the value of Y2:"))
        return ((self.X2 - self.X1)**2 + (self.Y2 - self.Y1)**2)**0.5

Ed=Euclidean()
ed=Ed.num()
print(f"The value of ED is {ed}")
