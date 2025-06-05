from itertools import accumulate
n = int(input())
l = list(map(int,input().split()))

l2 = []
for i in l:
    l2.append(i)

l2.sort()

pre1 = list(accumulate(l))
pre2 = list(accumulate(l2))

for i in range(int(input())):
    t, left, right = map(int,input().split())
    if t == 1:
        if left == 1:
            print(pre1[right-1])
        else:
            print(pre1[right-1] - pre1[left-2])
    else:
        if left == 1:
            print(pre2[right-1] )
        else:
            print(pre2[right-1] - pre2[left-2])