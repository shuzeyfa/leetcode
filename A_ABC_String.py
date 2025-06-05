for _ in range(int(input())):
    n, z = map(int,input().split())
    l = list(map(int,input().split()))
    for i in range(n):
        l[i] = l[i] | z
    print(max(l))