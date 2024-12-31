"""
Implement a recursive function to calculate the factorial of a number
"""

def factorial(n: int):
    """
    Function to calculate factorial of a positive number
    """
    if n < 0:
        return None
    
    # TODO: Base condition
    # We know that 0! = 1
    if n == 0:
        return 1

    return n * factorial(n-1)

print(factorial(-1))