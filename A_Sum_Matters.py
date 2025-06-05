for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    b = []
    summ1 = sum(l)
    summ2 = 0
    if n == 1:
        print("NO")
    else:
        for i in l:
            if i == 1:
                b.append(2)
            else:
                b.append(1)
        s = sum(b)
        if s > summ1:
            print("NO")
        else:
            print("YES")