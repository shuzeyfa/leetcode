for _ in range(int(input())):
    n, k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    count=summ=0
    for i in range(n):
        summ += l[i]
        if summ/(i+1)<k:
            break
        count+=1
    print(count)
    