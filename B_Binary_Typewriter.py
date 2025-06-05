from collections import deque
for _ in range(int(input())):
    n = int(input())
    s = input()
    ind = 0
    maxx = 0
    zero = 0
    one = 0
    for i in range(n):
        if s[i] == "0":
            zero += 1
        else:
            one += 1
    if zero == n:
        print(n)
    elif one == n:
        print(n+1)
    else:
        block = 0
        sign = "0"
        for i in range(n):
            if s[i] != sign:
                block += 1
                sign = s[i]
        
        tot = 0
        ind2 = 0
        sign = int(s[0])
        
        while ind2<n:
            if ind2 == 0:
                if s[ind2] == "0":
                    tot += 1
                else:
                    tot += 2
                ind2 += 1
            elif s[ind2] == str(sign):
                tot += 1
                ind2 += 1
            else:
                tot += 2
                sign = int(s[ind2])
                ind2 += 1
        if block <=1:
            print(tot)
        elif block == 2:
            print(tot-1)
        else:
            print(tot-2)

       