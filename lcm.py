# Uses python3
####import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_efficient(a,b):
    
    if a < b :
        a,b = b,a
    
    while b > 0:
        a,b = b, a%b
        
    return a


def lcm_efficient(a,b):
    return a*b//gcd_efficient(a,b)


if __name__ == '__main__':
####    input = sys.stdin.read()
####    a, b = map(int, input.split())
    a, b = map(int, input().split())
#    print(lcm_naive(a, b))
    print(lcm_efficient(a, b))
