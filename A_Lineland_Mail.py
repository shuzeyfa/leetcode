n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    if i == 0:
        print(abs(l[i]-l[1]),abs(l[-1]-l[0]))
    elif i == n-1:
        print(abs(l[-1]-l[-2]),(abs(l[-1]-l[0])))
    else:
        print(min(abs(l[i]-l[i+1]),abs(l[i]-l[i-1])),  max( abs(l[i]-l[-1]) ,abs(l[i]-l[0])))