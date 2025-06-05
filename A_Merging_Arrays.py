n ,k =map(int,input().split())
l = list(map(int,input().split()))
l2 = list(map(int,input().split()))

for i in range(k):
    j = i
    while j>0 and l2[j-1]>l2[j]:
        l2[j-1],l2[j] = l2[j],l2[j-1]
        j -= 1
print(*l2)