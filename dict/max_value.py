# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}

# max_value_key(my_dict))
#
# Output:
# b

def max_value_key(my_dict):
    max, index = 0, ""
    for key in my_dict:
        if my_dict[key] > max:
            max = my_dict[key]
            index = key
    return index

print(f"Max value key: {max_value_key(my_dict)}")
    