for _ in range(int(input())):
    n = int(input())
    l=[]
    for i in range(n):
        s = input()
        l.append(s.index("#")+1)
    l.reverse()
    print(*l)