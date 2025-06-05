n,m = map(int,input().split())
left= []
right = []
for i in range(m):
    s= input()
    if s[7] == "r":
        right.append(int(s[-1]))
    else:
        left.append(int(s[-1]))
if len(right) > 0 and len(left)>0:
    maxx = min(left)
    minn = max(right)
    if maxx > minn:
        val = (maxx - minn) - 1
        print(val if val >0 else -1)
    else:
        print(-1)
elif left:
    val = (min(left)-1)
    print(val if val > 0 else -1)

elif right:
    val = (n- max(right))
    print(val if val > 0 else -1)
    
else:
    print(n)
