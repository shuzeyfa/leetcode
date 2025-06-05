for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    s = ""
    for i in range(1,13):
        if i == a or i== b:
            s += "a"
        elif i == c or i == d:
            s += "b"
    if s=="abab" or s=="baba":
        print("YES")
    else:
        print("NO")
