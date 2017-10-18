# Uses python3


#result = 0
#
#for i in range(0, n):
#    for j in range(i+1, n):
#        temp =  a[i]*a[j]
#        if temp > result:
#            result = temp

def max_multi_fast(n,a):

    idx1 = 0 
    for i in range(0, n):
        if a[i] > a[idx1]:
                idx1 = i

    idx2 = -1
    for i in range(0, n):
        # check that the current index is not equal to the first index,
        # and that the current index has not been set or if set,
        # the value of the current index is greater than the value of the prior index.
        if i != idx1 and (idx2 == -1 or a[i] > a[idx2]): 
            idx2 = i

    result =  a[idx1]*a[idx2]
    return(result)

#how_many = int(input())
#number_list = [int(x) for x in input().split()]
#assert(len(number_list) == how_many)

import numpy as np
np.random.seed(1)
#if __name__ == '__main__':
while True:
    how_many = np.random.randint(2,high=1000)
    print(how_many)
    number_list = [np.random.randint(1,high=100000) for i in range(how_many)]
    print(len(number_list))

    print(max_multi_fast(how_many,number_list))

