for _ in range(int(input())):
    input()  
    k, n, m = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    
    i, j = 0, 0  
    b = []  
    t = True
    while i < n or j < m:
        if i < n and l1[i] == 0:  
            b.append(0)
            k += 1
            i += 1
        elif j < m and l2[j] == 0:  
            b.append(0)
            k += 1
            j += 1
        elif i < n and l1[i] <= k:  
            b.append(l1[i])
            i += 1
        elif j < m and l2[j] <= k:
            b.append(l2[j])
            j += 1
        else:  
            print(-1)
            t=False
            break
    if t == True:
        print(*b)
    