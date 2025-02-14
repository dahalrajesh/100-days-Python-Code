def remove_duplicates(lst):
    unique_list = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

# Example usage
my_list = [1, 2, 3, 2, 4, 1, 5, 6, 3, 7]
print(remove_duplicates(my_list))
