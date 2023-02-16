""" the original code
def func(n): 
if n == 0 or n == 1: 
return n 
else: 
return func(n-1) + func(n-2)
"""

#version of the code with memoization 

def fib(n, dict={}):
    if n in dict:
        return dict[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = fib(n-1, dict) + fib(n-2, dict)
        dict[n] = result
        return result
