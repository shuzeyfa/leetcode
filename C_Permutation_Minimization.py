from collections import deque
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    de = deque()

    for i in l:
        if len(de) == 0:
            de.append(i)
        else:
            if i <= de[0]:
                de.appendleft(i)
            else:
                de.append(i)
    print(*de)