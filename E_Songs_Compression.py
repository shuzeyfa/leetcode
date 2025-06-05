n,m =map(int,input().split())
a = []
b = []
for i in range(n):
    left, right = map(int,input().split())
    a.append(left)
    b.append(right)
summ = sum(a)
rem = summ - m if summ - m >0 else 0
if summ <= m:
    print(0)
elif sum(b)>m:
    print(-1)
else:
    dif = []
    for i in range(n):
        dif.append(a[i]-b[i])
    dif.sort(reverse=True)
    count = 0
    ind = 0
    while rem >0:
        count += 1
        rem -= dif[ind]
        ind += 1
    print(count)
