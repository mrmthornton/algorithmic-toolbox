# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

#result = 0
#
#for i in range(0, n):
#    for j in range(i+1, n):
#        temp =  a[i]*a[j]
#        if temp > result:
#            result = temp

idx1 = 0
for i in range(0, n):
    if a[i] > a[idx1]:
        idx1 = i

idx2 = 0
for i in range(0, n):
    if a[i] > a[idx2] and a[i] != a[idx1]:
        idx2 = i

        result =  a[idx1]*a[idx2]

print(result)
