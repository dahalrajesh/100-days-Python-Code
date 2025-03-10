def calculate_sum_and_average():
    numbers = []
    
    while True:
        num = float(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        numbers.append(num)

    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0  # Avoid division by zero

    print(f"Total Sum: {total_sum}")
    print(f"Average: {average}")

# Run the function
calculate_sum_and_average()
