for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    high = []
    low = []
    for i in range(n):
        if a[i]>= b[i]:
            high.append(a[i])
            low.append(b[i])
        else:
            high.append(b[i])
            low.append(a[i])
    summ = sum(high)
    low.sort(reverse=True)
    summ += sum(low[:k-1])
    print(summ +1)