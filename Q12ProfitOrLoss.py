# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
while True:
    try:
        # User Inputs
        cost_price = int(input("Enter the cost price:"))
        Selling_price=int(input("Enter the selling price:"))

        # Checking Whether Positive Or Negative mean profit or loss

        if cost_price<Selling_price:
            profit = Selling_price - cost_price
            print(f"it is a profit{profit}.")
        elif Selling_price==cost_price:
            print("No loss and Profit.")
        else:
            loss = cost_price - Selling_price
            print(f"It is a loss{loss}")

        # I ask User perception
        user_input=input("Do  you want to Continue?(yes/no)")
        if user_input!='yes':
            break
    except ValueError:
        print("Enter the Valid inputs ,It must be Integers.")
