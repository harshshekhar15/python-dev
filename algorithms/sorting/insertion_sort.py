"""
Implement Insertion sort in python
"""


def insert(alist, index, n):
    #code here
    j = index
    while j>0 and alist[j-1]>alist[j]:
        alist[j-1], alist[j] = alist[j], alist[j-1]
        j -= 1
    
#Function to sort the list using insertion sort algorithm.    
def insertionSort(alist, n):
    #code here
    for i in range(n):
        insert(alist, i, n)

new_array = [13,46,24,52,20,9]
insertionSort(new_array, len(new_array))
print(new_array)