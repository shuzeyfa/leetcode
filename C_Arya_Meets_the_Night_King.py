from collections import defaultdict
n,k=map(int,input().split())
l=list(map(int,input().split()))
d=defaultdict(int)
for i in range(k):
    temp1,temp2 = map(int,input().split())
    d[temp1]+=temp2
l2=[]
ind = defaultdict(int)
for i in range(n):
    ind[i] = l[i]
l.sort()

d3=defaultdict(int)
val=list(d.keys())
val.sort()
ind2 = 0
summ=0
for i in range(n):
    while ind2<len(val) and l[i]>=val[ind2]:
        summ+=d[val[ind2]]
        ind2+=1
    d3[l[i]] = summ
l4 = [0]*n
for i in range(n):
    temp=ind[i]
    l4[i] = d3[temp]
print(*l4)