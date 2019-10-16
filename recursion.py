#recursive function for calculating factorial
def fact(n):
    if n >= 0:
        if n >= 1:
            return n * fact(n-1)
        else:
            return 1
    else:
        return "n must be a positive integer"

'''
print(fact(2))
print(fact(8))
print(fact(0))
print(fact(-1))
'''

#recursive function for fibonacci series
def fib(n):
    if n >= 0:
        if n >= 2:
            return fib(n-1) + fib(n-2)
        elif n == 0 or n == 1:
            return n
        #same code as above, just longer 
        #elif n == 1:
            #return 1
        #else:
        #    return 0
    else:
        return "n must be a positive integer"

print (fib(4))
print (fib(2))
print (fib(6))
print (fib(0))
