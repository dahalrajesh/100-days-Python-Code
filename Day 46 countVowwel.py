# Get user input
text = input("Enter a string: ")

# Define vowels (both uppercase and lowercase)
vowels = "aeiouAEIOU"

# Count vowels using list comprehension
vowel_count = sum(1 for char in text if char in vowels)

# Display the result
print("Number of vowels:", vowel_count)
