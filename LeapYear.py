# This Python program determines whether a given year is a leap year or not, 
# using both object-oriented programming (OOP) principles and user-friendly interaction.
# user_input=int(input("Enter the year for checking leap year or Not?"))
# if user_input%400==0:
#     print(f"The {user_input} is leap Year.")
# elif user_input%100==0:
#     print(f"The {user_input} is not leap Year.")
# elif user_input%4==0:
#     print(f"The {user_input} is leap Year.")
# else:
#     print(f"The {user_input} is not leap Year")
class Year:
    # constructor is not necessary to do here because it is not used outside the function.
    def __init__(self):
        self.user_input=0

    def check_leap_year(self):
        while True:
            try:
                self.user_input = int(input("Enter the year for checking leap year or Not:"))
                if self.user_input%400==0:
                    print(f"The {self.user_input} is leap Year.")
                elif self.user_input%100==0:
                    print(f"The {self.user_input} is not leap Year.")
                    break
                elif self.user_input%4==0:
                    print(f"The {self.user_input} is leap Year.")

                else:
                    print(f"The {self.user_input} is not leap Year")

                if input("Do you want to check another year? (yes/no): ").lower() != "yes":
                    break

            except ValueError:
                print("Enter the valid Number.")
leapyear=Year()
leapyear.check_leap_year()