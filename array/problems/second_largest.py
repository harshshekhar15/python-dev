"""
Given an array of integers return the second largest and the second smallest integer
from the array
"""
import sys

def find_second_largest(arr):
    largest = arr[0]
    slargest = -1
    
    for i in range(1, len(arr), 1):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] > slargest and arr[i] != largest:
            slargest = arr[i] 
    
    return slargest

def find_second_smallest(arr):
    smallest = arr[0]
    ssmallest = sys.maxsize
    
    for i in range(1, len(arr), 1):
        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]
        elif arr[i] < ssmallest and arr[i] != smallest:
            ssmallest = arr[i]
    
    return ssmallest
            


def find_second(arr):
    slargest = find_second_largest(arr)
    ssmallest = find_second_smallest(arr)
    return [slargest, ssmallest]



new_array = [10001,50,10,5,30,88,56,100001]
print(find_second(new_array))