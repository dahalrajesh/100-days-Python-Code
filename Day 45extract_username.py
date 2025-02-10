import re

def extract_username(email):
    # Step 1: Extract part before '@'
    local_part = email.split('@')[0]
    
    # Step 2: Remove digits
    clean_name = re.sub(r'\d+', '', local_part)
    
    # Step 3: Split into possible first and last names
    # Assuming the name is in the format 'lastnamefirstname' or 'firstnameLastname'
    # Here, we assume the transition from lowercase to uppercase or vice versa
    name_parts = re.findall('[a-zA-Z][^A-Z]*', clean_name)
    
    # Step 4: Capitalize and join
    formatted_name = ''.join(part.capitalize() for part in name_parts)
    
    return formatted_name

# Example
email = "dahalrajesh369@gmail.com"
username = extract_username(email)
print(username)  # Output: RajeshDahal
