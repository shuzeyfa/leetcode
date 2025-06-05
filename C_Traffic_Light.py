for _ in range(int(input())):
    temp,char = input().split()
    n = int(temp)
    s=input()

    find = []
    g = []
    for i in range(n):
        if s[i] == "g":
            g.append(i)
        elif s[i] == char:
            find.append(i)
    
    maxx = float("-inf")

    def check(val,g2):
        low = 0
        high = len(g2) - 1
        ind = float("inf")
        while low<=high:
            mid = (low+high)//2
            if g2[mid] > val:
                ind = g2[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ind


    if char == "g":
        print(0)
    else:
        for i in find:
            val2 = check(i,g)
            if val2 == float("inf"):
                temp2 = n - (i+1)
                count = g[0] + 1
                maxx = max(temp2 + count,maxx)
            else:
                temp2 = val2 - i
                maxx = max(maxx,temp2)
        print(maxx)

