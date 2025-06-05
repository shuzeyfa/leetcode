n, k = map(int,input().split())
l = list(map(int,input().split()))
temp = l[:k]
summ = sum(temp)
sum2 = summ
count = 1
left=0
for i in range(k,n):
    summ += l[i]
    summ -= l[left]
    sum2 += summ
    left += 1
    count += 1
print("%.10f" % (summ))