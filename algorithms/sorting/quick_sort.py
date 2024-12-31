"""
Implement Quick sort algorithm in python


Quick sort:
- Select a pivot index and place it on the index where it will lie in the
  sorted array
- Move all the items lesser than pivot element to the left side of the pivot
  and the greater items to the right of the pivot in the array
- Repeat the same steps recursively for the elements placed to the left and
  right side of the pivot element.
  
NOTE: We'll be selecting the starting index as the pivot for simplicity but
      any index can be chosen as the pivot
"""


def find_pivot_index(arr, low, high):
    """
    Find the correct index of the pivot, place
    it on that index and returns that index
    """
    pivot = low
    i = low
    j = high
    
    while i<j:
        while arr[i] <= arr[pivot] and i < high:
            i += 1
        while arr[j] > arr[pivot] and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j
    

def quick_sort(arr, low, high):
    if low < high:
        print(f"Running quick sort for {low} to {high}")
        pivot_index = find_pivot_index(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)
    else:
        return

new_array = [13,46,24,52,20,9,1]
quick_sort(new_array, 0, len(new_array)-1)
print(new_array)
