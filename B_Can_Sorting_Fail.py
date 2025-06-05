from collections import deque
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    
    nums=l[:]
    nums.sort()
    t=True
    for i in range(n):
        if nums[i]!=l[i]:
            print("YES")
            t=False
            break
    if t==True:
        print("NO")
            

    
    