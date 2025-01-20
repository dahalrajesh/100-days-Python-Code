# Write a program that will tell the number of dogs and chicken are
# there when the user will provide the value of total heads and legs.
from numpy.testing.print_coercion_tables import print_new_cast_table


def predict():
    head=int(input("Enter the number of head:"))
    legs=int(input("Enter the number of legs"))
    if legs % 2 != 0 or legs < 2 * head or legs > 4 * head:
        print("Invalid input! Please ensure the number of heads and legs are valid.")
        return

# suppose I used the equation of method rule:
# if I have x+y=head mean chicken+dogs=head
# chicken has 2 legs and dogs has 4 legs mean 2x+4y=total legs by the equation we get
# 2*(x+y)=2*head and 2x+4y=total legs
# 2x is cut then we have y=total legs- 2 head//2 where y is dogs

    dogs=(legs-2*head)//2
    chicken=head-dogs
    print(f"The number of dogs is {dogs}")
    print(f"The Number of chicken is {chicken}")
predict()
