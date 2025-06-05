from collections import Counter
for _ in range(int(input())):
    s=input()
    p=input()
    q=input()
    i,j = 0,0
    while i<len(s) and j<len(p):
        if s[i]==p[j]:
            i+=1
        j+=1
    if i!=len(s):
        print("NO")
    else:
        d1=Counter(s+q)
        d2=Counter(p)
        t=True
        for i in d2:
            if d2[i]>d1[i]:
                print("NO")
                t=False
                break
        if t==True:
            print("YES")

