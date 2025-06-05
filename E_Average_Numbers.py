from itertools import accumulate
n = int(input())
l = list(map(int,input().split()))
l2=list(accumulate(l))
summ=l2[-1]
l3=[]

for i in range(n):
    temp = summ-l[i]
    if temp/(n-1) == l[i]:
        l3.append(i+1)
print(len(l3))
print(*l3)