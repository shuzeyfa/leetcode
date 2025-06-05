for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    tot = 0
    i = 0
    while i < len(l)-1:
        if l[i] > l[i+1]:
            tot += 1
            i += 1
        i += 1

    print(tot)
