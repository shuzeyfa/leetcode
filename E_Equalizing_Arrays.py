n = int(input())
l1 = list(map(int,input().split()))
m = int(input())
l2 = list(map(int,input().split()))
if sum(l1)!=sum(l2):
    print(-1)
else:
    ans = 0
    i,j = 0,0
    cur1, cur2 = 0 ,0
    while i<n:
        cur1 += l1[i]
        cur2 += l2[j]
        i += 1
        j += 1
        while cur1 != cur2:
            if cur1<cur2:
                cur1 += l1[i]
                i += 1
            else:
                cur2 += l2[j]
                j += 1
        ans += 1
    print(ans)