n, m=map(int,input().split())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    if i==0:
        l.append(a*b)
    else:
        l.append(l[-1]+(a*b))
l2 = list(map(int,input().split()))
ind=1
j=0

for i in l2:
    while i>l[j]:
        j+=1
        ind+=1
    print(ind)