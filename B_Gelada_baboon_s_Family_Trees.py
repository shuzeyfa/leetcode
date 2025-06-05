from collections import defaultdict
n = int(input())
l = list(map(int,input().split()))

rank = [0 for i in range(n)]
parent = {i:i for i in range(n)}

def find(x):
    rep_x = parent[x]
    if rep_x == x:
        return x
    while parent[x] != x:
        x = parent[x]
    return x



def union(x,y):
    rep_x = find(x)
    rep_y = find(y)
    if rep_x != rep_y:
        if rank[rep_x] > rank[rep_y]:
            parent[rep_y] = rep_x
        elif rank[rep_x] < rank[rep_y]:
            parent[rep_x] = rep_y
        else:
            parent[rep_x] = rep_y
            rank[rep_y] += 1

for i in range(n):
    union(i,l[i]-1)

s= set()
for i in range(n):
    val = find(i)
    s.add(val)
print(len(s))
