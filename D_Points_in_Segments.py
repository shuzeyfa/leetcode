n, m =map(int,input().split())
l = [0]*m
for i in range(n):
    left, right = map(int,input().split())
    l[left-1] += 1
    if right<m:
        l[right]-=1


for i in range(1,m):
    l[i] += l[i-1]
ans=[]
for i in range(m):
    if l[i] == 0:
        ans.append(i+1)
if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(*ans)