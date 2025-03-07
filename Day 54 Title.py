def to_title_case(s):
    words = s.split()  # Split the string into words
    title_case_words = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    return ' '.join(title_case_words)
input_string = "hello world!"
output_string = to_title_case(input_string)
print(output_string) 
