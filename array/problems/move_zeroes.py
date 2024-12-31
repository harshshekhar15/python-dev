"""
Move all zeroes to end of array

Given an array arr[]. Push all the zeros of the given array to the right 
end of the array while maintaining the order of non-zero elements. Do the 
mentioned change in the array in place.
"""

def pushZerosToEnd(arr):
    j = 0
    while arr[j] != 0 and j < len(arr)-1:
        j += 1
    i = j+1
    while i < len(arr):
        if arr[i] == 0:
            i += 1
        else:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            i += 1