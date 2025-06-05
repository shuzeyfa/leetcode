for _ in range(int(input())):
    n = input()
    s = input()
    l = s.split("<")
    l2 = s.split(">")
    maxx = 0
    for i in range(len(l)):
        maxx = max(maxx, len(l[i]))
    for j in range(len(l2)):
        maxx = max(maxx, len(l2[j]))
    print(maxx + 1)