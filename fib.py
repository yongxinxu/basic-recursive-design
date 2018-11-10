def fib(n):
    precondition(is_integer(n) and n > 0)
    
    if n == 1:
        return 1
    elif n ==2:
        return 1
    else:
        assert n > 2
        return fib(n-1) + fib(n-2)
 
    
    # postcondition: fib(n) is the positive integer which is the n-th element of the Fibonacci Sequence.
    #                To more specific, fib(n) is the sum of fib(n-1) and fib(n-2), when n >= 3. And fib(1) and fib(2) are 1 
