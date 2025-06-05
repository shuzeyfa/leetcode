k = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
count = 0
summ = 0
for i in range(len(l)):
    if summ >= k:
        break
    summ += l[i]
    count += 1
if summ>=k:
    print(count)
else:
    print(-1)
