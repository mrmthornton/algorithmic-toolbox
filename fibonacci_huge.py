# Uses python3
####import sys
import timeit

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_efficient(n,m):
    d, sequence = find_pattern(n,m)
    if d == -1:
        print("ERROR, array not large enough?")
        return None
    index = n%d
    return sequence[index]


def find_pattern(n,m):
    SIZE = 500000
    
    if n <= 1:
        return (m, [0,1])

    previous = 0
    current  = 1
    #start_time = timeit.default_timer() #for debug
    ####a = [None for _ in range(SIZE)]
    a = [0,1]
    #print(timeit.default_timer()-start_time) #for debug
    a[1] = 1

    #start_time = timeit.default_timer() #for debug
    while True:
        previous, current = current, (previous + current)%m
        ####a[i] = current
        a.append(current)
        if previous == 0 and current == 1:
            #print(timeit.default_timer()-start_time) #for debug
            return (len(a)-2, a)
            
    return (-1,-1) # error if reaches here       
    
    
if __name__ == '__main__':
####    input = sys.stdin.read();
####    n, m = map(int, input.split())
    n, m = map(int, input().split())
#    print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_efficient(n, m))
