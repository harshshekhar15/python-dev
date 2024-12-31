def fib(num):
    if num < 0 or int(num) != num:
        raise Exception("Numbers can be positive integers only")
    if num in [0,1]:
        return num
    else:
        # print(num)
        return fib(num-1) + fib(num-2)

print(fib(35))