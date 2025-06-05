for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = []

    for i in range(n):
        count = 1
        ind = i
        while l[ind] != i+1:
            ind = l[ind] -1
            count += 1
        ans.append(count)
    print(*ans)
