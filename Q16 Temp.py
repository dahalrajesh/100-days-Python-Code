# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool 

while True:
    temp = int(input("Enter the Temperature of the weather (°C): "))
    humidity = int(input("Enter the Humidity of the weather (%): "))

    # Determine the weather condition
    if temp >= 30 and humidity >= 90:
        print("Weather: Hot and Humid")
    elif temp >= 30 and humidity < 90:
        print("Weather: Hot")
    elif temp < 30 and humidity >= 90:
        print("Weather: Cool and Humid")
    elif temp < 30 and humidity < 90:
        print("Weather: Cool")

    # Ask the user if they want to continue
    user_input = input("Do you want to continue? Enter Yes or No: ").strip().lower()

    # Break the loop if the user enters "no"
    if user_input == "no":
        print("Exiting the program. Goodbye!")
        break
