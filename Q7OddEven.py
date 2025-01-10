# Write a program that will tell whether the number entered by the user is odd or even.
# user_input=int(input("Enter the Number: "))
# if user_input%2==0:
#     print(f" {user_input}  is Even.")
# else:
#     print(f" {user_input} is Odd.")

# If I want try Using OPPS:
# Class name should be in Pascal case.
class OddEven:
    def __init__(self):
        self.user_input=0
    def num_checker(self):
        while True:
            try:
                self.user_input = input("Enter the Number else if you want to exit the Program write exit in Lower Case: ")
                if self.user_input.lower()=='exit':
                    print("See you again,Good Bye!")
                    break
                self.user_input=int(self.user_input)
                if self.user_input%2==0:
                    print(f" {self.user_input}  is Even.")

                else:
                    print(f" {self.user_input} is Odd.")
                break
            except ValueError:
                print("Try the Integers NUmber,Invalid Number!")
Num=OddEven()
Num.num_checker()


