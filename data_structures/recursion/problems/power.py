"""
Find the power of a number using recursion
"""

def power(base, expo: int) -> int:
    if expo == 0:
        return 1
    elif expo < 0:
        return 1/base * power(base, expo + 1)
    return base * power(base, expo - 1)

print(power(2,-2))