import math
for _ in range(int(input())):
    n, k =map(int,input().split())
    ele=n//2
    find=n-ele
    if n%2==0:
        find+=1
    print(k//find)