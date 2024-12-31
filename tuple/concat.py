# Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

# Example

input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

def concat_tuple(input_tuple):
    # res = ""
    # for i in input_tuple:
    #     res = res + " " + i
    # return res
    return ' '.join(input_tuple)

print(concat_tuple(input_tuple))