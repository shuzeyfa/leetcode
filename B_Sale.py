n, m =map(int,input().split())
l = list(map(int,input().split()))
l2 = []
for i in range(n):
    if l[i] <0:
        l2.append(l[i])
l2.sort()
if len(l2)<=m:
    print(-sum(l2))
else:
    print(-sum(l2[:m]))