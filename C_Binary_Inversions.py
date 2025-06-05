for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    one = 0
    zero = 0
    for i in range(n):
        if l[i] == 0:
            zero += 1
        else:
            one += 1
    if one == n or zero == n:
        print(n-1)
    else:
        l2 = l[:]
        l3 = l[:]
        for i in range(n):
            if l[i] == 0:
                l[i] = 1
                break
        for i in range(n-1,-1,-1):
            if l2[i] == 1:
                l2[i] = 0
                break
        zero = 0
        count1 = count2 = 0
        for i in range(n-1,-1,-1):
            if l[i] == 0:
                zero += 1
            else:
                count1 += zero
        zero = 0
        for i in range(n-1,-1,-1):
            if l2[i] == 0:
                zero += 1
            else:
                count2 += zero
        zero = 0
        count3 = 0
        for i in range(n-1,-1,-1):
            if l3[i] == 0:
                zero += 1
            else:
                count3 += zero

        print(max(count1,count2,count3))
        
