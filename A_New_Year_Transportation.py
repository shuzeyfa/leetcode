n , k = map(int,input().split())
l = list(map(int,input().split()))


t = False
ind = 1
while ind<= n:
    if ind == k:
        t = True
        print("YES")
        break
    elif ind > k:
        break
    ind = ind + l[ind-1]

if t == False:
    print("NO")
