for _ in range(int(input())):
    n,k = map(int,input().split())
    s=input()
    black = 0
    for i in range(k):
        if s[i]=="B":
            black += 1
    if black>= k:
        print(0)
    else:
        white = k - black
        right,left = k,0
        minn = white
        while right<len(s):
            if s[right] == "B":
                black += 1
            else:
                white += 1
            if s[left] == "B":
                black -= 1
            else:
                white -= 1
            minn = min(minn,white)
            left += 1
            right+=1
        print(minn)