"""
Convert a decimal number to binary using recursion
"""

def binary(num: int) -> int:
    # if num < 0:
    #     raise Exception("Number cannot be negative")
    # Base condition: When quotient is zero stop recursion
    if num == 0:
        return 0
    
    return num % 2 + 10 * binary(int(num / 2))

print(binary(-12))