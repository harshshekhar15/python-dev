"""
Right rotate an array by d places

"""

def reverse(arr, low, high):
    start = low
    end = high
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr, d):
    d = d % len(arr)
    reverse(arr, 0, d-1)
    reverse(arr, d, len(arr)-1)
    reverse(arr, 0, len(arr)-1)


def right_rotate(arr, d):
    d = d % len(arr)
    left_rotate(arr, len(arr)-d)
    

new_array = [1,2,3,4,5,6,7]
left_rotate(new_array, 2)
print(new_array)
right_rotate(new_array, 2)
print(new_array)