import heapq
from collections import Counter,deque
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d=Counter(l)
    l2 = list(d.values())
    maxx = max(l2)
    if maxx <= n/2:
        print(n%2)
    else:
        if maxx == n:
            print(n)
        else:
            rem = n - maxx
            print(maxx - rem)
            




        
            

    

