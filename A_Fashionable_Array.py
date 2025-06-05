for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    evenfirst = evensec = oddfirst = oddsec = float("inf")
    for i in range(n):
        if l[i] % 2 == 0:
            evenfirst = i
            break
    for i in range(n):
        if l[i] % 2 == 1:
            oddfirst = i
            break
    for i in range(n-1,-1,-1):
        if l[i] % 2 == 0:
            evensec = i
            break
    for i in range(n-1,-1,-1):
        if l[i] % 2 == 1:
            oddsec = i
            break
    
    if oddsec == float("inf") and oddfirst == float("inf"):
        print(evenfirst+(n-(evensec+1)))
    elif evensec == float("inf") and evenfirst == float("inf"):
        print(oddfirst+(n-(oddsec+1)))
    else:
        val1 = (evenfirst+(n-(evensec+1)))
        val2 = (oddfirst+(n-(oddsec+1)))
        print(min(val1,val2))
    