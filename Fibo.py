

def fibo(i):
    if i == 0:
        return 0
    elif i ==1:
        return 1
    else:
        return fibo(i-2) + fibo(i-1)
    
for x in range(10):
    print(fibo(x))



# Memorization

fibonacci_cache = {}

def fibonacci(n):
    # if we have the cached value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    #Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range (1, 1001):
    print(n, ":", fibonacci(n))