from collections import deque
n, k = map(int,input().split())
s1 = input()
s2 = input()

q = deque([(0,1,0)])
visited = set([(0,1,0)])
time = 0
t = "NO"
while q:
    cur,sign,time = q.popleft()
    
    if cur+k >= n:
        t = "YES"
        break

    if sign == 1:
        if cur - 1 >=0 and cur-1>time and s1[cur-1]!="X" and (cur-1,sign) not in visited:
            visited.add((cur-1,sign,time+1))
            q.append((cur-1,sign,time+1))
        if s1[cur+1] != "X" and (cur+1,sign) not in visited:
            visited.add((cur+1,sign,time+1))
            q.append((cur+1,sign,time+1))
        if s2[cur+k] != "X" and (cur+k,2) not in visited:
            visited.add((cur+k,2,time+1))
            q.append((cur+k,2,time+1))
    if sign == 2:
        if cur - 1 >=0 and cur-1>time and s2[cur-1]!="X" and (cur-1,sign) not in visited:
            visited.add((cur-1,sign,time+1))
            q.append((cur-1,sign,time+1))
        if s2[cur+1] != "X" and (cur+1,sign) not in visited:
            visited.add((cur+1,sign,time+1))
            q.append((cur+1,sign,time+1))
        if s1[cur+k] != "X" and (cur+k,1) not in visited:
            visited.add((cur+k,1,time+1))
            q.append((cur+k,1,time+1))
    
    # print(q)
print(t)
