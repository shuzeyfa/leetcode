import heapq
l = [4, 1, 3, 9, 7]
heapq.heapify(l)

nums = []
while l:
    nums.append(heapq.heappop(l))


print(nums)