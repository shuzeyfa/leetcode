for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    ans = []
    if n == 1:
        print(0)
    else:
        for i in range(0,len(l),2):
            if l[i]>l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
            ans.append([l[i],l[i+1]])
        ans.sort()
        t = 1
        val = []
        print(ans)
        for i in range(len(ans)):
            val.extend(ans[i])
        for i in range(1,n):
            if val[i]<val[i-1]:
                t = -1
                break
        print(t)
