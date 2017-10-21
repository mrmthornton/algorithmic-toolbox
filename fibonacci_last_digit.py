# Uses python3
####import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def efficient_last_digit(n):
    
    if n <= 1:
        return n
    
    a = [0]*(n+1)
    a[1] = 1
    previous = 0
    current  = 1   
    
    for i in range(2,n+1):
        previous, current = current, (previous + current)%10
        a[i] = current 
    
    return a[n]


if __name__ == '__main__':
####    input = sys.stdin.read()
    n = int(input())
##    print(get_fibonacci_last_digit_naive(n))
    print(efficient_last_digit(n))