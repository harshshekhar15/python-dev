"""
Implement Merge sort in python
"""

def merge(arr, l, m, r): 
    # code here
    res = []
    left = l
    right = m+1
    while left<=m and right<=r:
        if arr[left] <= arr[right]:
            res.append(arr[left])
            left += 1
        else:
            res.append(arr[right])
            right += 1
    while left <= m:
        res.append(arr[left])
        left += 1
    while right <= r:
        res.append(arr[right])
        right += 1
    # Update the arr with res
    for i in range(l, r+1, 1):
        arr[i] = res[i-l]   
        
        
def mergeSort(arr, l, r):
    #code here
    if l == r:
        return
    mid = (l+r)//2
    # print(mid)
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)

new_array = [13,46,24,52,20,9,1]
mergeSort(new_array, 0, len(new_array)-1)
print(new_array)