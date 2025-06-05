for _ in range(int(input())):
    n, f, a, b = map(int,input().split())
    l = list(map(int,input().split()))
    t = True
    for i in range(n):
        temp = (l[i] - l[i-1] if i>0 else l[i])*a
        temp2 = b
        temp3 = min(temp,temp2)
        if temp3 < f:
            f -= temp3
        else:
            t = False
            print("NO")
            break

    if t == True:
        print("YES")
        
