"""
Find the GCD of two numbers using recursion
"""

def gcd(num1, num2: int) -> int:
    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)

print(gcd(18,48))