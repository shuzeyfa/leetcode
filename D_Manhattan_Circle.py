for _ in range(int(input())):
    n ,m =map(int,input().split())
    l = []
    for i in range(n):
        l.append(input())
    row= col = float("inf")
    t=False
    for i in range(n):
        for j in range(m):
            if l[i][j] == "#":
                row = i
                col = j
                t=True
                break
        if t==True:
            break
    temp1,temp2 = row, col
    count = 0
    while temp1 <n and l[temp1][temp2] == "#":
        count +=1
        temp1+=1
    print(row+1+(count//2),col+1)
