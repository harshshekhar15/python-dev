"""
Module that contains a decorator for logging the time taken
"""

def time_logger(func):
    """
    Decorator that logs the time taken to execute a function
    """
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to execute {func.__name__}: {end-start} seconds")
        return result
    return wrapper