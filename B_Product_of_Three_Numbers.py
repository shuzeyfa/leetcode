for _ in range(int(input())):
    n = int(input())

    ans= []
    count = 0
    i = 2
    while i*i<=n:
        if n%i==0:
            count += 1
            ans.append(i)
            n = n // i
        i+=1
        if count==2:
            ans.append(n)
            break
    if count<2:
        print("NO")
    elif ans[0]==ans[2] or ans[1]==ans[2]:
        print("NO")
    else:
        print("YES")
        print(ans[0],ans[1],ans[2])