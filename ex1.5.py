import time
import matplotlib.pyplot as plt

# original Fibonacci function
def func(n): 
    if n == 0 or n == 1: 
        return n 
    else: 
        return func(n-1) + func(n-2) 

# memoized Fibonacci function
def fib(n, dict={}):
    if n in dict:
        return dict[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = fib(n-1, dict) + fib(n-2, dict)
        dict[n] = result
        return result

# time both functions for input values between 0 and 35
input_values = range(36)
func_times = []
fib_times = []
for i in input_values:
    start_time = time.time()
    result = func(i)
    end_time = time.time()
    func_times.append(end_time - start_time)
    
    start_time = time.time()
    result = fib(i)
    end_time = time.time()
    fib_times.append(end_time - start_time)

# plot the results
plt.plot(input_values, func_times, label='Original')
plt.plot(input_values, fib_times, label='Memoized')
plt.xlabel('Data')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
