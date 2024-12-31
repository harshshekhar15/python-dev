"""
Write a function to return the nth number in the Fibonacci sequence.

Two methods:
- Memoization: Storing the sub-problems output in array and using it wherever
               required again.
- Tabulation

"""
# from data_structures.utils.time_logger import time_logger
import time

# @time_logger

def fibonacci_using_memoization(n: int, dp: list[int]) -> int:
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibonacci_using_memoization(n-1, dp) + fibonacci_using_memoization(n-2, dp)
    return dp[n]

def fibonacci_using_tabulation(n:int) -> int:
    dp = [-1 for i in range(n+2)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+2):
        dp[i] =  dp[i-1] + dp[i-2]
    return dp[n]

def fibonacci_using_tabulation_optimized(n:int) -> int:
    prev2 = 0
    prev = 1
    for i in range(2, n+1):
        curri = prev + prev2
        prev2 = prev
        prev = curri
    return curri

if __name__ == "__main__":
    n = 100
    dp = [-1 for i in range(n+2)]
    start = time.time()
    print(f"Fibonacci number at {n}: {fibonacci_using_memoization(n, dp)}")
    end = time.time()
    print(f"Total execution time: {end-start}")
    
    start2 = time.time()
    print(f"Fibonacci number at {n} using tabulation: {fibonacci_using_tabulation_optimized(n)}")
    end2 = time.time()
    print(f"Total execution time: {end2-start2}")