for _ in range(int(input())):
    n,k,q = map(int,input().split())
    l = list(map(int,input().split()))
    right = 0
    count = 0
    while right < n:
        if l[right] <= q:
            left = right
            while right < n and l[right] <= q:
                right += 1
            if (right - left) >= k:
                ind = right - left - k + 1
                count += (ind*(ind+1))//2
    
        else:
            right += 1
    print(count)
    