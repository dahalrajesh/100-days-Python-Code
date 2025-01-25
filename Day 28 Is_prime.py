num = int(input("Enter the number: "))

if num <= 1:
    print(f"The given number {num} is not a prime number.")
else:
    is_prime = True  # Assume the number is prime initially
    for i in range(2, num // 2 + 1):  # Check up to num // 2
        if num % i == 0:  # If num is divisible by any number other than 1 and itself
            is_prime = False
            break

    # Print the result after the loop
    if is_prime:
        print(f"The given number {num} is a prime number.")
    else:
        print(f"The given number {num} is not a prime number.")
