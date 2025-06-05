from itertools import accumulate
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int,input().split()))

    m = int(input())
    l2 = list(map(int,input().split()))

    pre1 = list(accumulate(l1))
    pre2 = list(accumulate(l2))

    first = max(0,max(pre1))
    second = max(0,max(pre2))

    print(first + second)
