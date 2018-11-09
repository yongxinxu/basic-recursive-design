"""
##############################################################################
#
>>> fib(1)
1

>>> fib(2)
1

>>> fib(3)
2

>>> fib(6)
8

>>> fib(12)
144

#
##############################################################################

##############################################################################
#
# Design notes: 
# 1. Identify a smaller instance of problem: n==(n-1)
# 2. Express solution to general problem in terms of solution to smaller instance: fib((n-1)-1) + fib((n-1)-2)
# 3. base cases, smallest cases, no recursion: n==1
# 4. answer to base case: 1
# 5. show that program eventually reaches base case: subtracting 1 from n, you eventually reach 1
#
##############################################################################

"""

from math import *
# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)
    

def fib(n):
    precondition(is_integer(n) and n > 0)
    
    if n == 1:
        return 1
    elif n ==2:
        return 1
    else:
        assert n > 2
        return fib(n-1) + fib(n-2)
    #

    
    # postcondition: fib(n) is the positive integer which is the n-th element of the Fibonacci Sequence.
    #                To more specific, fib(n) is the sum of fib(n-1) and fib(n-2), when n >= 3. And fib(1) and fib(2) are 1 
    
    # postcondition collaborator: Huanyu Zhang
    

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
