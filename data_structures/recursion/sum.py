"""
Find the sum of the digits of a positive number using recursion
"""

def sum(number: int) -> int:
    if number < 0:
        raise Exception("Number should be a positive number")
    if number == 0:
        return 0
    remainder = int(number % 10)
    dividend = number // 10
    print(f"Number: {number}\nRemainder: {remainder}\nDividend: {dividend}")
    return remainder + sum(dividend)

# def sum_using_fact(number, n: int) -> int:
#     if n == 1:
#         return number[1]
#     else:
#         return sum_using_fact(number, n-1)
    

print(sum(11212))