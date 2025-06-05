for  _ in range(int(input())):
    n = int(input())
    s = input()
    tot = 0
    for i in s:
        if i == "1":
            tot += 1
    
    count = 0
    for i in s:
        if i == "1":
            count += (tot-1)
        else:
            count += (tot+1)
    print(count)