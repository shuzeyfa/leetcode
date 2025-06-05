from bisect import bisect_left
for _ in range(int(input())):
    n, cur = input().split()
    s = input()
    if cur == "g":
        print(0)
    else:
        n = int(n)
        g = []
        l = []
        for i in range(n):
            if s[i] == "g":
                g.append(i)
            elif s[i] == cur:
                l.append(i)
        minn = 0
        for i in range(len(l)):
            ind = bisect_left(g,l[i])
            if ind == len(g):
                rem = n - l[i]
                val = rem + g[0]
            else:
                val = g[ind] - l[i]
            minn = max(minn, val)
        print(minn)
        