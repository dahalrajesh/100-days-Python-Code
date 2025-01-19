def menu():
    while True:
        print("\nMenu:")
        print("1. Convert cm to ft")
        print("2. Convert km to miles")
        print("3. Convert USD to INR")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                # cm to ft
                cm = float(input("Enter the length in cm: "))
                feet = cm / 30.48  # 1 ft = 30.48 cm
                print(f"{cm} cm is equal to {feet:.2f} ft")
            
            elif choice == 2:
                # km to miles
                km = float(input("Enter the distance in km: "))
                miles = km * 0.621371  # 1 km = 0.621371 miles
                print(f"{km} km is equal to {miles:.2f} miles")
            
            elif choice == 3:
                # USD to INR
                usd = float(input("Enter the amount in USD: "))
                inr = usd * 82.50  # Example conversion rate (update as needed)
                print(f"${usd} USD is equal to ₹{inr:.2f} INR")
            
            elif choice == 4:
                # Exit
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please choose a valid option from the menu.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

# Call the menu function
menu()
