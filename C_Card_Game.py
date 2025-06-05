for _ in range(int(input())):
    a,b,c,d= map(int,input().split())
    count1 = c2 = 0
    tot = 0
    r1=0
    r2=0
    if a>c:
        r1+=1
    elif c>a:
        r2+=1

    if b>d:
        r1+=1
    elif d>b:
        r2+=1

    if r1>r2:
        tot += 2

    r3=r4=0
    if b>c:
        r3+=1
    elif c>b:
        r4+=1

    if a>d:
        r3+=1
    elif d>a:
        r4+=1

    if r3>r4:
        tot += 2
    
    

    print(tot)