"""
Implement Bubble sort in python
"""

def bubbleSort(arr, n):
    for i in range(n-1, 0, -1):
        didSwap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = True
        if not didSwap:
            return

new_array = [13,46,24,52,20,9,1]
bubbleSort(new_array, len(new_array))
print(new_array)