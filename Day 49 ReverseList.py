# Method 1: Using slicing
def reverse_list_slicing(lst):
    return lst[::-1]

# Method 2: Using the reverse() method
def reverse_list_method(lst):
    lst.reverse()
    return lst

# Method 3: Using the reversed() function
def reverse_list_function(lst):
    return list(reversed(lst))

# Method 4: Using a loop
def reverse_list_loop(lst):
    reversed_lst = []
    for item in lst[::-1]:
        reversed_lst.append(item)
    return reversed_lst

# Example usage
original_list = [1, 2, 3, 4, 5]
print("Original List:", original_list)
print("Reversed (Slicing):", reverse_list_slicing(original_list))
print("Reversed (reverse method):", reverse_list_method(original_list.copy()))
print("Reversed (reversed function):", reverse_list_function(original_list))
print("Reversed (Loop):", reverse_list_loop(original_list))
