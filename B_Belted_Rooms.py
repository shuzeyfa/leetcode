for _ in range(int(input())):
    n = int(input())
    s = input()
    c = cc = False
    for i in s:
        if i == ">":
            c= True
        elif i=="<":
            cc= True
    if c and cc:
        s += s[0]
        ans = 0
        for i in range(n):
            if s[i] == "-" or s[i+1] == "-":
                ans += 1
        print(ans)

    else:
        print(n)