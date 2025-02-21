# Reverse words in a given string

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage
original_string = "Hello how are you"
print("Original String:", original_string)
print("Reversed Words:", reverse_words(original_string))
