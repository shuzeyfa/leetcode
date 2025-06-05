n , k = map(int,input().split())
count = 0
for i in range(n):
    s1, s2 = input().split()
    if s1 == "+":
        k += int(s2)
    else:
        if int(s2)<= k:
            k -= int(s2)
        else:
            count += 1

print(k,count)