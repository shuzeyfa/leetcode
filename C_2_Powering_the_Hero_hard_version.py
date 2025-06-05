import heapq
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    nums = []
    heapq.heapify(nums)
    tot = 0
    for i in range(n):
        if l[i] == 0:
            if len(nums) > 0:
                tot += -heapq.heappop(nums)
        else:
            heapq.heappush(nums,-l[i])
    print(tot)

    
