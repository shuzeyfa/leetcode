for _ in range(int(input())):
    n = int(input())
    l = []
    low=0
    high=float("-inf")
    for i in range(n):
        temp = list(map(int,input().split()))
        high=max(high, temp[1])
        l.append(temp)
    
    ans = float("inf")

    def check(val):
        le,ri = 0,0
        for i in l:
            if i[1]<le:
                if le - val <= i[1]:
                    le = max(i[0],le-val)
                    ri = i[1]
                else:
                    return False
            else:
                if ri + val >= i[0]:
                    le = i[0]
                    ri = min(i[1],ri+val)
                else:
                    return False
        return True


    while low<=high:
        mid = (low+high) // 2
        if check(mid):
            ans=min(mid,ans)
            high=mid-1
        else:
            low=mid+1
    print(ans)