# Reverse words in a given string

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage
original_string = "Hello how are you"
print("Original String:", original_string)
print("Reversed Words:", reverse_words(original_string))

# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num = 5
print("Factorial of", num, "is", factorial(num))
