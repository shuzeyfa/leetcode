n, k =map(int,input().split())
guests = []
for i in range(k):
    u,v = map(int,input().split())
    guests.append((u,v))
    
flavor_demand = [0] * (n + 1)
for a, b in guests:
    flavor_demand[a] += 1
    flavor_demand[b] += 1

guests.sort(key=lambda x: flavor_demand[x[0]] + flavor_demand[x[1]])

used = [False] * (n + 1)
sad_guests = 0

for a, b in guests:
    if not used[a]:
        used[a] = True
    elif not used[b]:
        used[b] = True
    else:
        sad_guests += 1
print(sad_guests)
