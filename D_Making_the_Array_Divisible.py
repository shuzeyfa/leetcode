from collections import defaultdict
for _ in range(int(input())):
    n, k =map(int,input().split())
    l = list(map(int,input().split()))
    d=defaultdict(int)
    for i in l:
        mod=i%k
        rem=k-mod
        if rem!=k:
            d[rem] += 1
    
    li = []
    for i in d:
        tot = 0
        tot += i
        rem = d[i] - 1
        tot += (k*rem)
        li.append(tot+1)
    print(max(li) if len(li)>0 else 0)