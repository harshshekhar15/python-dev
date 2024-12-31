"""
Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

Examples

flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]
"""


def flatten(arr):
    result = []
    
    for item in arr:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))