import math

n = int(input())
m = int(input())
l = []
for i in range(n):
    temp = int(input())
    l.append(temp)

maxx = max(l)
summ = sum(l) + m
print(max(math.ceil(summ/n),maxx), maxx+m)
