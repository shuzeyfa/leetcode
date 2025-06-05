for _ in range(int(input())):
    n = int(input())
    s = input()
    maxx = 0
    for i in s:
        val = ord(i)
        maxx = max(val-ord("a") + 1,maxx)
    print(maxx)