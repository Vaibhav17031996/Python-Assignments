list = list(range(1, 11))
extracted_list = list[:5]
reversed_list = extracted_list[::-1]

# Aliter: Using built-in functions
# reversed_list = list(reversed(extracted_list))
# extracted_list.reverse()    // extracted_list itself is changed (no separate variable(reversed_list) is required).

print(f"Original list: {list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")