from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = defaultdict(list)
    d[0].extend(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    l2 = []
    for i in l:
        val = d[i].pop()
        l2.append(val)
        d[i+1].append(val)
    print("".join(l2))
    