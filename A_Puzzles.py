n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
minn = l[n-1]-l[0]
left = 1
for i in range(n,m):
    minn = min(minn, l[i]-l[left])
    left+=1
print(minn)