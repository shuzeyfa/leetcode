from collections import deque
n, k =map(int,input().split())
l = list(map(int,input().split()))

left = 0
count =0 
dec = deque()
inc = deque()

for i, num in enumerate(l):
    while dec and dec[-1] < num:
        dec.pop()
    dec.append(num)

    while inc and inc[-1] > num:
        inc.pop()
    inc.append(num)

    while dec[0] - inc[0] > k:
        if dec[0] == l[left]:
            dec.popleft()
        if inc[0] == l[left]:
            inc.popleft()
        left += 1
    count += (i - left + 1)
print(count)
    
    
