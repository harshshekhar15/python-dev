"""
Given an array of length N, where each element denotes the position of a stall. Now you have N stalls and an
integer K which denotes the number of cows that are aggressive. To prevent the cows from hurting each other,
you need to assign the cows to the stalls, such that the minimum distance between any two of them is as large as
possible. Return the largest minimum distance.
Eg

array: 1,2,4,8,9  &  k=3
O/P: 3
Explanation: 1st cow at stall 1 , 2nd cow at stall 4 and 3rd cow at stall 8
"""
from typing import List

def cows_placed(stalls: List[int], min_distance, total_cows: int) -> bool:
    last = stalls[0]
    cows_positioned = 1
    for i in range(1, len(stalls)):
        if stalls[i] - last >= min_distance:
            cows_positioned += 1
            last = stalls[i]
    if cows_positioned >= total_cows:
        return True
    else:
        return False
            

def assign_cows(stalls: List[int], cows: int) -> int:
    # Sort the stalls
    stalls.sort()
    low = 0
    high = stalls[len(stalls)-1] - stalls[0]
    min_distance = 0
    while low<=high:
        mid = (high + low) // 2
        if cows_placed(stalls, mid, cows):
            min_distance = mid
            low = mid + 1
        else:
            high = mid - 1
    return min_distance

array= [1,2,4,8,9]
k=3
print(f"Min distance: {assign_cows(array,k)}")