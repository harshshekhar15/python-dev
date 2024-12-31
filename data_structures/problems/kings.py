"""
Problem Statement:

In the land of Nomansland, the government wants to elect a new king based on the popularity of its
citizens. Each of the n citizens, is assigned a power value based on their popularity.
To be eligible to become the king, a person's power value K must satisfy  a special condition:
there must be another person in Nomansland whose power value X is equal to the total power of all
citizens excluding the potential king K.
Given the power values of all the citizens, determine how many people can be nominated as the king.

Constraints:
- 1 <= n <= 10^6
- 1 <= power of a person <= 10^6

Output format:
- Return an integer denoting the number of possible candidates for a king.

Example:

- Input : [1,2,3,4]
  Output: 2
"""

from typing import List

def sum(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[len(arr)-1] + sum(arr[:len(arr)-1])

def findCandidates(powers: List[int]) -> int:
    candidates = 0
    totalPower = sum(powers)
    for i in range(len(powers)):
        for j in range(len(powers)):
            if i == j:
                continue
            if totalPower - powers[i] - powers[j] == powers[j]:
                print(f"Power: {powers[i]}, index: {i}")
                candidates += 1
    return candidates

powers = [5,2,3,5]
print(findCandidates(powers))