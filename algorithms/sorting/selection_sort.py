"""
Implement selection sort in Python


Algorithm:
- Identify the minimum element's index in the unsorted part of the array
- Swap the minimum element with the starting index of the unsorted part.

Time complexity: O(N^2) as we're using two loops

GeeksforGeeks problem - https://www.geeksforgeeks.org/problems/selection-sort/1
"""
from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def selectionSort(arr,n):
    #code here
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


new_array = [13,46,24,52,20,9]
print(selectionSort(new_array, len(new_array)))

