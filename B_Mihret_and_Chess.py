r1,c1,r2,c2 = map(int,input().split())
ans = []
if r1==r2 and c1==c2:
    print(0,0,0)
else:
    if r1 == r2 and c1 == c2:
        ans.append(0)
    elif r1== r2 or c2==c1:
        ans.append(1)
    else:
        ans.append(2)

    l1 = [(1,1),(1,3),(1,5),(1,7),(3,1),(3,3),(3,5),(3,7),(5,1),(5,3),(5,5),(5,7),(7,1),(7,3),(7,5),(7,7) ,(2,2),(2,4),(2,6),(2,8),(4,2),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,8),(8,2),(8,4),(8,6),(8,8)]
    first = set(l1)
    l2=[(1,2),(1,4),(1,6),(1,8),(3,2),(3,4),(3,6),(3,8),(5,2),(5,4),(5,6),(5,8),(7,2),(7,4),(7,6),(7,8), (2,1),(2,3),(2,5),(2,7),(4,1),(4,3),(4,5),(4,7),(6,1),(6,3),(6,5),(6,7),(8,1),(8,3),(8,5),(8,7)]
    sec= set(l2)
    if (r1,c1) in first:
        if (r2,c2) in first:
            if abs(r1-r2)==abs(c1-c2):
                ans.append(1)
            else:
                ans.append(2)
        else:
            ans.append(0)
    else:
        if (r2,c2) in sec:
            if abs(r1-r2)==abs(c1-c2):
                ans.append(1)
            else:
                ans.append(2)
        else:
            ans.append(0)

    temp = max(abs(r1-r2),abs(c1-c2))
    ans.append(temp)
    print(*ans)
     