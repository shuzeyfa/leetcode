for _ in range(int(input())):
    n = int(input())
    if n<10:
        print(n)
    elif n>45:
        print(-1)
    else:
        l = []
        for i in range(9,0,-1):
            if n>=i:
                l.append(str(i))
                n-=i


        l.sort()
        print("".join(l))


            
