# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def efficient_fib(n):
    
    if n <= 1:
        return n
    
    a = [0]*(n+1)
    a[1] = 1
    
    for i in range(2,n+1):
        a[i] = a[i-1] + a[i-2]
    
    return a[n]


n = int(input())
#print(calc_fib(n))

print(efficient_fib(n))

