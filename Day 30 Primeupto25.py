def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_first_25_primes():
    count = 0
    num = 2
    while count < 25:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

# Call the function to print the first 25 prime numbers
print_first_25_primes()
