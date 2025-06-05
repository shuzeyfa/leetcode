for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    gelly = min(a,c)
    flower  = min(b,d)
    if gelly >= flower:
        print("Gellyfish")
    else:
        print("Flower")