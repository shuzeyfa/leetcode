for _ in range(int(input())):
    n = int(input())
    s = input()
    l = []
    ind = n
    for i in range(n-1,-1,-1):
        if s[i]==")":
            l.append(s[i])
        else:
            break
    count = n - len(l)
    if count>=len(l):
        print("No")
    else:
        print("Yes")
    
